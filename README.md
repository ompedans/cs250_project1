# Omer Eren, Project 1 Report

## Design and implementation

For the first part of the project I used AflPlusPlus. Mainly, I am using the QEMU mode and running 3 instances of AFLPlusPlus to increase
the chances of finding a crash.

Here is the configuration I used for the 3 instances:
- Instance 1: With `-Q`, `-c 0`, and `AFL_COMPCOV_LEVEL=2`. This will enable logging of comparison operands and those logs will be used by various
mutators in AFL.
- Instance 2: with `-Q` and `AFL_USE_QASAN=1`. This will enable adress sanitation in QEMU mode, which will help my program to catch memory leaks
as opposed to just catching crashes.
- Instance 3: with `-Q` and `AFL_PRELOAD=libcmpcov.so` + `AFL_COMPCOV_LEVEL=2`. This will enable instrumentation of some cmp functions. I am not sure this will be helpful, since it seems like it only works when the binary is dynamically linked as opposed to statically linked.

I choose to go with AFLPlusPlus, since, in my opinion, it was the most extensive fuzzer available and most of the recent fuzzing research is already implemented into it. Hongfuzz was the other option I tried briefly, but it was way slower to find crashes in my experience.

## Usage

My small python executor script together with a Dockerfile is available at 
https://github.com/ompedans/cs250_project1. To setup, you can simply run
```
docker build -t omer_project -f Dockerfile .
```

Then, to run the project for a given binary
```
docker run -v [PATH_TO_BINARY_FOLDER]:/shared -it omer_project bash
```

Now, we are in the docker terminal and can simply run
```
python run.py [PATH_TO_BINARY]
```

This will start the AFL with the explained config and will store the result in `/shared/output/` with exact same format as AFLPlusPlus.

## Evaluation

Evaluation results can be found in the github repo under `EVALUATION.md`.

