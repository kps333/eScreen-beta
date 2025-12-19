from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess
import sys
import os
import urllib.request
import tempfile
import shutil

class InstallCommands(install):
    """自定义安装后命令来配置环境"""
    def run(self):
        # 先执行标准安装
        install.run(self)

        # 检查conda环境
        
        if 'CONDA_PREFIX' in os.environ:
              self.PACKAGEMANAGER = 'conda'
        elif 'MAMBA_PREFIX' in os.environ:
              self.PACKAGEMANAGER = 'mamba'
        else:
             return 1
        
        try:
            subprocess.run(["nvidia-smi"], capture_output=True, check=True)
            print("[Info] Find GPU")
        except:
            print("[Warning] No GPU detected.")

        steps = [
            self._install_pytorch,
            self._install_cuda_tools,
            self._install_flash_attention,
            self._install_flash_fft_conv,
            #self._install_jupyter_kernel
        ]

        INFOS = [
             'Setup PyTorch......',
             'Setup CUDA Tools......',
             'Setup Flash Attention......',
             'Setup Flash FFT Conv......',
             #'Setup Dependencies......'
        ]

        for i, step in enumerate(steps, 1):
            print(f"\n[ {i}/{len(steps)} ] {INFOS[i-1]}")
            if not step():
                return 2
            
    def _install_pytorch(self):
        """安装PyTorch"""
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install",
                "torch==2.6.0", "torchvision==0.21.0", "torchaudio==2.6.0",
                "--index-url", "https://download.pytorch.org/whl/cu118"
            ])
            return True
        except Exception as e:
            print(f"Failed to install PyTorch: {e}")
            return False
    
    def _install_cuda_tools(self):
        """安装CUDA工具"""
        try:
            subprocess.check_call([
                self.PACKAGEMANAGER, "install", "-c", "nvidia", "cuda-nvcc", "cuda-cudart-dev", "-y", "--quiet"
            ])
            return True
        except:
            print("Failed to install CUDA tools.")
            return False
    
    def _install_flash_attention(self):
        """安装Flash Attention"""
        
        # 方法1：尝试直接安装
        try:
            env = os.environ.copy()
            env['MAX_JOBS'] = '4'
            subprocess.check_call([
                sys.executable, "-m", "pip", "install",
                "flash-attn==2.7.3", "--no-build-isolation"
            ], env=env)
            return True
        except:
            pass
        
        # 方法2：下载预编译包
        try:
            python_version = f"cp{sys.version_info.major}{sys.version_info.minor}"
            wheel_url = (
                f"https://github.com/Dao-AILab/flash-attention/releases/download/"
                f"v2.7.3/flash_attn-2.7.3+cu11torch2.6cxx11abiTRUE-"
                f"{python_version}-{python_version}-linux_x86_64.whl"
            )
            with tempfile.NamedTemporaryFile(suffix='.whl', delete=False) as tmp:
                urllib.request.urlretrieve(wheel_url, tmp.name)
                subprocess.check_call([
                    sys.executable, "-m", "pip", "install", tmp.name
                ])
            return True
        except Exception as e:
            print(f"Failed to install Flash Attention: {e}")
            return False
    
    def _install_flash_fft_conv(self):
        """安装flash-fft-conv"""
        temp_dir = tempfile.mkdtemp(prefix="flash_fft_conv_")
        try:
            # 克隆仓库
            repo_url = "https://github.com/HazyResearch/flash-fft-conv.git"
            clone_dir = os.path.join(temp_dir, "flash-fft-conv")
            subprocess.check_call(["git", "clone", repo_url, clone_dir])
            # 安装子模块
            os.chdir(os.path.join(clone_dir, "csrc", "flashfftconv"))
            subprocess.check_call([sys.executable, "setup.py", "install"])
            # 安装主包
            os.chdir(os.path.join(clone_dir))
            subprocess.check_call([sys.executable, "setup.py", "install"])
            return True
        except Exception as e:
            print(f"Failed to intall Flash FFT Conv: {e}")
            return False
        finally:
            # 清理临时目录
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir, ignore_errors=True)
            os.chdir(os.path.dirname(os.path.abspath(__file__)))       

setup(name='escreen',
      version='0.0.0',
      description='Using Deep Learning to screen functional cis-regulatory elements in silico',
      url='https://github.com/kps333/eScreen-beta/tree/main',
      author='Liquan Lin, Shijie Luo',
      author_email='21620241153548@stu.xmu.edu.cn, sluo112211@163.com',
      license='GNU',
      packages=find_packages(include=['escreen']),
      python_requires='>=3.10',
      cmdclass={'install': InstallCommands,},
      install_requires=[
          'pyBigWig',
          'pyfaidx',
      ]
    )