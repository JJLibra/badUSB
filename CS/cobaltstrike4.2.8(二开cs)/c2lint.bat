@echo off
java -Dfile.encoding=UTF-8 -XX:ParallelGCThreads=4 -XX:+UseParallelGC -classpath ./cobaltstrike.jar c2profile.Lint %*
