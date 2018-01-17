FROM nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04

RUN apt update && apt install -y \
    python3 \
    python3-dev \
    python3-pip \
    python3-setuptools

RUN pip3 install \
  ipython \
  numpy \
  pandas \
  scipy \
  sklearn \
  jupyter \
  && \
 python3 -m ipykernel.kernelspec

EXPOSE 8888

RUN pip3 install http://download.pytorch.org/whl/cu80/torch-0.3.0.post4-cp35-cp35m-linux_x86_64.whl \
   torchvision

COPY tools/jupyter_notebook_config.py  /root/.jupyter/

CMD jupyter notebook --ip=* --allow-root
