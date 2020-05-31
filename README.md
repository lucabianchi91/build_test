# build_test

To reproduce the build issue, clone and run
`docker build -t build_test .`

This should result in `AttributeError: module 'queue' has no attribute 'Full'`

If `eventlet` is removed from `pathex`, build succed, but
`docker run -it --rm build_test` will fail at runtime with 
```
ModuleNotFoundError: No module named 'eventlet.hubs.epolls'
[6] Failed to execute script build_test
```
Please note that the script works fine with the interpreter.
To verify it:
```
docker run -it --rm --entrypoint="" build_test python3 /root/build_test/build_test.py
```

