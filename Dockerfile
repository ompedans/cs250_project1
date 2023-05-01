FROM aflplusplus/aflplusplus:latest

RUN cd /AFLplusplus && make -j `nproc` all && cd qemu_mode && ./build_qemu_support.sh

WORKDIR /home/omer

COPY . ./

ENTRYPOINT "/bin/bash"