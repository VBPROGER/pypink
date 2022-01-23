#!/usr/bin/python3
'''INITIALIZATION CODE STARTS HERE'''

ru, en = 'ru', 'en'

import os, platform
from random import choice
try:
    import atexit
except ImportError:
    raise ImportError('Library "atexit" isn'+"'"+'t installed.')
class main_error(Exception):
    def __init__(self, pass_on_error = True, *args) -> None:
        pass
class runtime_error(Exception):
    def __init__(self, pass_on_error = True, *args) -> None:
        pass
class import_error(Exception):
    def __init__(self, pass_on_error = True, *args) -> None:
        pass
class code_error(Exception):
    def __init__(self, pass_on_error = True, *args) -> None:
        pass
class env_error(Exception):
    def __init__(self, pass_on_error = True, *args) -> None:
        pass


class EmptyStringError(Exception):
    def __init__(self, pass_on_error = True, *args) -> None:
        pass
class InvalidStringError(Exception):
    def __init__(self, pass_on_error = True, *args) -> None:
        pass
class InvalidStringType(Exception):
    def __init__(self, pass_on_error = True, *args) -> None:
        pass
class UnsupportedStringType(Exception):
    def __init__(self, pass_on_error = True, *args) -> None:
        pass
class TooManyNotStringsInString(Exception):
    def __init__(self, pass_on_error = True, *args) -> None:
        pass


class env:
    env_list = ['none.temporary-env-file']
    def __init__(self, *args) -> None:
        pass
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
    def __init__(self, *args) -> None:
        pass
    def exit_handler():
        try:
            for get_env in env.env_list:
                try:
                    os.remove(get_env)
                except Exception:
                    pass
        except Exception:
            pass
atexit._clear()
atexit.register(__pypink__.exit_handler)

'''AND ENDS HERE. MAIN CODE STARTS HERE'''

def get_args(*args):
    return args
def clear_console(cross_platform = True, *args):
    if cross_platform == True:
        os.system('clear || cls || :')
    else:
        if os.name.lower() == 'posix':
            os.system('clear')
        else:
            os.system('cls')
def capitalize(string = None, *args):
    is_string_empty = is_empty(string)
    if is_string_empty == False:
        return string.capitalize()
    else:
        return False
def is_empty(string = None, *args):
    if string == None or string == '':# or string.startswith(' ') and string.endswith(' '):
                                    # Removed this part due bugs and glitches
        return True
    else:
        return False
def platform_name():
    return str(platform.system()).lower()
def pip_install(lib: str, *args):
    is_string_empty = is_empty(lib)
    if not is_string_empty:
        if platform_name() == 'windows':
            os.system('py -m ensurepip --upgrade || cls; pip install '+str(lib))
        else:
            os.system('python -m ensurepip --upgrade || clear; pip install '+str(lib))
    else:
        pass
def crop_string(string = None, symbol = None, *args):
    if type(string).__name__ == 'str' or type(symbol).__name__ == 'str':
        if is_empty(string) or is_empty(string):
            raise EmptyStringError('Excepted str, instead got '+str('NoneType with empty input'))
        else:
            Splitted_List = string.split(str(symbol))
            return Splitted_List
    if 1==1:
        if type(string).__name__ != 'str':
            raise InvalidStringError('Excepted str, instead got '+str(type(string).__name__))
        elif type(symbol).__name__ != 'str':
            raise InvalidStringError('Excepted str, instead got '+str(type(symbol).__name__))
        else:
            if type(symbol).__name__ == 'str' or type(string).__name__ == 'str':
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
def pr(pr, raw = False, *args):
    if raw: pr = ''.join(r'{}'.format(pr))
    if pr != '':
        if str(type(pr).__name__) == 'str':
            if raw: print(r'{}'.format(pr))
            else: print(pr)
        else:
            raise ValueError('Excepted "str".type, instead got "{}.type"; use str() or \'quotes\' converter instead'.format(str(type(pr).__name__)))
    # A shorter and better version for "print"
def is_from_blacklist(string, blacklist, *args):
    if string in blacklist:
        return True
    else:
        return False
    # Simple blacklist engine
def random_string(length = 0, custom_strings_list = [], *args):
    string = ''
    strings_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g']
    if len(custom_strings_list) <= 0:
        for x in range(length): string += choice(strings_list)
    else:
        for x in range(length): string += choice(custom_strings_list)
    return string
    # Simple random string generator
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
def err_crashed(code = None, confirmation = False, *NoneArgs_pass):
    if confirmation: print('\033[0;31mpypink.Error: Crashed; "'+str(code)+str('"')+'\033[0m');exit()
def alphabet(lang = 'en', *args):
    def list_lang(lang):
        en = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        ru = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
        if lang == 'en':
            return en
        elif lang == 'ru':
            return ru
    if stringmngr_is_string(lang):
        return list_lang(lang)
    else: return False

def stringmngr_is_string(string, *args):
    if stringmngr_is_string_is_type(string, 'str'): return True
    else: return False
def stringmngr_is_int(string, *args):
    if stringmngr_is_string_is_type(string, 'int'): return True
    else: return False
def stringmngr_is_float(string, *args):
    if stringmngr_is_string_is_type(string, 'float'): return True
    else: return False

def stringmngr_is_string_is_type(string, is_type, *args):
    if stringmngr_get_string_type(string) == is_type: return True
    else: return False
def stringmngr_get_string_type(string, *args): return str(type(string).__name__)
'''AND ENDS HERE.'''

'''TESTING AREA IS HERE'''

# Enter your code here

'''AND TESTING AREA ENDS HERE.'''