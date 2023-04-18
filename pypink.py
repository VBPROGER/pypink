#!/usr/bin/python3
__version__ = '0.0.1'
ru, en = 'ru', 'en'

import os, platform
from random import choice
try:
    import atexit
except ImportError:
    raise ImportError('Library "atexit" isn\'t installed.')
class main_error(Exception):
    def __init__(self, pass_on_error: bool = True, *args) -> None:
        self.pass_on_error, self._called_args = pass_on_error, args
class runtime_error(main_error): pass
class import_error(main_error): pass
class code_error(main_error): pass
class env_error(main_error): pass

class EmptyStringError(main_error): pass
class InvalidStringError(main_error): pass
class InvalidStringType(main_error): pass
class UnsupportedStringType(main_error): pass
class TooManyNotStringsInString(main_error): pass

class env:
    env_list = ['none.temporary-env-file']
    def __init__(self, *args) -> None: self._call_args = args
    def create(self = None, name = None, file = None, value = '', *args) -> None:
        if value == '' or name == '' or file == '' or value == None or name == None or file == None:
            raise env_error('env.create: env name / value / file name cannot be empty\nvalues: {NAME:"'+str(name)+'",FILE:"'+str(file)+'",VALUE:"'+str(value)+'"}')
        else:
            if not name in env.env_list and not file in env.env_list and not file + '.temporary-env-file' in env.env_list:
                with open(file + '.temporary-env-file', 'w') as File:
                    File.write(str(name).replace('\n',''))
                    File.write('\n'+str(value).replace('\n',''))
                    File.close()
                env.env_list.append(file + '.temporary-env-file')
            else:
                raise env_error('env.create: env name / file name have been already declared\nvalues: {NAME:"'+str(name)+'",FILE_NAME:"'+str(file)+'"}')
class __pypink__:
    def __init__(self, *args) -> None: self._call_args = args
    def exit_handler(self):
        try:
            for get_env in env.env_list:
                try: os.remove(get_env)
                except BaseException as e: continue
        except BaseException as e: return e
__pypink__ = __pypink__()
atexit._clear()
atexit.register(__pypink__.exit_handler)

def get_args(*args): return args
def clear_console(cross_platform: bool = True, *args):
    if cross_platform == True: os.system('clear || cls || :')
    else: return os.system('clear') if os.name.lower() == 'posix' else os.system('cls')
def capitalize(string = None, *args):
    if not is_empty(string): return string.capitalize()
    else: return False
def is_empty(string = None, *args): return ((not string) or string == '' or (not str(string).strip().lower()))
def platform_name(): return str(platform.system()).lower()
def pip_install(lib: str, *args):
    lib = str(lib)
    if not is_empty(lib):
        if platform_name() == 'windows': os.system('py -m ensurepip --upgrade || cls; pip install ' + lib)
        else: os.system('python -m ensurepip --upgrade || clear; pip install ' + lib)
    else: return False
def crop_string(string: str = '', symbol: str = '', *args):
    if type(string).__name__ == 'str' or type(symbol).__name__ == 'str':
        if is_empty(string) or is_empty(string):
            raise EmptyStringError('Excepted str, instead got '+str('NoneType with empty input'))
        else:
            Splitted_List = string.split(str(symbol))
            return Splitted_List
        if not stringmngr_is_string(string): raise InvalidStringError('Excepted str, instead got ' + stringmngr_get_string_type(string))
        elif not stringmngr_is_string(symbol): raise InvalidStringError('Excepted str, instead got ' + stringmngr_get_string_type(symbol))
        else:
            if stringmngr_is_string(string) or stringmngr_is_string(symbol):
                pass
            else:
                raise code_error('Unexpected error: expected str, instead got NoneType and got invalid input type')
def llama_sh(command = 'echo "llama_sh v.1.0.0"', *args):
    try:
        if str(type(command).__name__) == 'str':
            os.system(str(command))
        else:
            raise UnsupportedStringType('Excepted str, instead got '+str(type(command).__name__))
    except TypeError:
        raise TooManyNotStringsInString('Got too many invalid strings')
def pr(s: str = '', no_newline: bool = False, raw: bool = False, *args) -> None:
    if raw: s = ''.join(r'{}'.format(s))
    if s and stringmngr_is_string(s):
        print(s, end = '' if no_newline else '\n')
    else:
        raise ValueError('Excepted "str".type, instead got "{}.type"; use str() or \'quotes\' converter instead'.format(stringmngr_get_string_type(s)))
def is_from_blacklist(string, blacklist, *args): return (string in blacklist)
def random_string(length = 0, custom_strings_list = [], *args):
    string = ''
    strings_list = alphabet()
    if len(custom_strings_list) <= 0:
        for x in range(length): string += choice(strings_list)
    else:
        for x in range(length): string += choice(custom_strings_list)
    return string
def custom_raise(raise_class = runtime_error, raise_description = '', exit_after = True, exit_code = 0, *args):
    try:
        print('The current program "'+str(get_program_name())+'" raises an error: ')
        print('   pypink.raise(){')
        print('   [          '+str(raise_class.__name__)+',')
        if not is_empty(str(raise_description)):
            print('   [          '+str(raise_description)+',')
        else: print('   ][')
        print(']}')
        if exit_after:
            try: exit(int(exit_code))
            except BaseException: return False
    except BaseException as e: err_crashed(code = e, confirmation = True)
def get_program_name(*args):
    return str(os.path.basename(__file__))
def err_crashed(code: str = '', confirmation: bool = False, exit_: bool = True, *NoneArgs_pass):
    if confirmation and str(confirmation).strip().lower():
        print('\033[0;31mpypink.Error: Crashed; "'+str(code)+str('"')+'\033[0m')
        if exit_: exit()
def alphabet(lang = en, upper: bool = True, *args):
    l_en = 'abcdefghijklmnopqrstuvwxyz'
    l_ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    if upper:
        l_en += l_en.upper()
        l_ru += l_ru.upper()
    l_en = list(l_en)
    l_ru = list(l_ru)
    return l_en if lang == en else l_ru
def stringmngr_is_string(string, *args): return stringmngr_is_stype(string, 'str')
def stringmngr_is_int(string, *args): return stringmngr_is_stype(string, 'int')
def stringmngr_is_float(string, *args): return stringmngr_is_stype(string, 'float')
def stringmngr_is_stype(string, is_type, *args): return stringmngr_get_string_type(string) == is_type
def stringmngr_get_string_type(string, *args): return str(type(string).__name__)
