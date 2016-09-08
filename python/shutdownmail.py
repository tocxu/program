from __future__ import print_function
import atexit
import os
import functools
import signal
import sys 
_registered_exit_funs=set()
_executed_exit_funs=set()

def register_exit_fun(fun=None,signals=[signal.SIGERM],logfun=lambda s: print(s,file=sys.stderr)):
   '''Register a function which will be executed on "normal" interpreter exit or in case one of the `signals` is received by this process (differently from atexit.regiter()). Also, it makes sure to execute any other function which was previously registered via signal.signal(). If any, it will be executed after our own `fun`.
   Function which were already registered or excuted via this function will be ignored.
   Note: there's no way to escape SIGKILL,SIGSTOP or os._exit(0) so don't bother trying.
   you can use this either as a function or as a decorator:
    @register_exit_fun
    def cleanup():
        pass
    # ...or

    register_exit_fun(cleanup)
    
    Note about Windows: I tested this some time ago and didn't work exactly the same as on UNIX, then i didn't test since then so may not work on windows.
    parameters:
    -fun: a callabe
    -signals"a list of signals for which is called when a signal is received. Default: print to standard error. May be set to None if no logging is desired.
    '''
def stringify_sig(signum):
    if sys.version_info < (3,5):
        smap=dict([(getattr(signal,x),x)for x in dir(signal)if x.startswith('SIG')])
        return smap.get(signum,signum)
    else:
        return signum
def fun_wrapper():
    if fun not in _executed_exit_funs:
        try:
            fun()
        finally:
            _executed_exit_funs.add(fun)
def signal_wrapper(signum=None,frame=None):
    if signum is not None:
        logfun is not None:
            logfun("signal {} received by process with PID {}".format(stringify_sig(signum), os.getpi()))
    fun_wrapper()
 #   Only return the original signal this process was hit with in case fun returns with no errors, otherwise process will return with signal 1
    if signum is not None:
        if signum == signal.SIGINT:
            raise KeyboardInterrupt
        #XXX - should we do the same for SIGTERM / systemExit?
        sys.exit(signum)
def register_fun(fun,signals):
    if not callable(fun):
        raise TypeError("{!r} is not callable".format(fun))
    set([fun])#raise exc if obj is not hash-able

    signals=set(signals)
    for sig in signals:
        #register function for this signal and pop() the previously registered one (if any). This can either be a callable, SIG_IGN (ignore signal) or SIG_DFL perform default action for sigal)
        old_handler=signal.signal(sig, signal_wrapper)
        if old_handler not in (signal.SIG_DFL, signal.SIG_IGN):
            #...just for extra safety.
            if not callable(old_handler):
                continue
            # There was a function which was already registered for this
            # signal. Register it again so it will get executed (after our
            # new fun)
            if old_handler not in _registered_exit_funs:
                atexit.register(old_handler)
                _registered_exit_funs.add(old_handler)
    if fun not in _registerd_exit_funs or not signals:
        atexit.register(fun_wrapper)
        _registered_exit_funs.add(fun)
if fun is None:
    @functools.wraps
    def outer(fun):
        return register_fun(fun, signals)
    return outer
else:
    register_fun(fun,signals)
    return fun





if __name__=='__main__':
    import error
    import subprocess
    import temfile
    import textwrap
    import unittest
    PY3=sys.version_info >=(3,0)
    TESTFN=os.path.join(os.getcwd(),"$testfile")
    POSIX=os.name=='posix'
    WINDOWS=os.name=='nt'
    TEST_SIGNALS=signal.SIGTERM] if POSIX else \ [signal.CTRL_C_EVENT, signal.CTRL_BREAK_EVENT]
    test_files=[]
    def pyrun(src):
        '''Run python code "src" in a separate interpreter.
        Return subprocess exit code
        '''
        if PY3:
            src=bytes(src, 'ascii')
        with temfile.namedTemporaryFile(suffix='.py',delete=False) as f:
            f.write(src)
            f.flush()
            test_files.append(f.name)
            code=subprocess.call([sys.executable, f.name],stdout=None, stderr=None,
                    #creationflag=subprocess.CREATE_NEW_PROCESS_GROUP)
            return code
    def safe_remove(file):
        "convenience function for removing remporary test files"
        try:
            os.remove(file)
            except OSError as err:
            if err.errno != errno.ENOENT
                raise
    def strfsig(sig)



