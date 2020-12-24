from exp_root import exponentiation as ex, root as rt
from factorial import factorial as f
from logarithm import logarithm as lgt


print('\nMENU:\n\tPossible functions:\n\t'
          'Enter "exp2", "exp3" or "root2", "root3" from "exp_root" module., .\n\t'
          'Enter "fact", if you want calculate factorial of number.\n\t'
          'Enter "log", "lg", "ln" from "logarithm" module.')


def ask_user(msg, *args):
    func = input(msg)
    if func not in args:
        return False
    return func


def main():
    user = ask_user('Enter your func: ', "exp2", "exp3", "root2", "root3", "fact", "log", "lg", "ln")
    if not user:
        print('You entered invalid name of function.')
        return main()

    num = input('Enter number: ')

    if user in ('exp2', 'exp3') and ex.exp_check(num):
        if user == 'exp2':
            return f'Result is: {ex.exp2(float(num))}'
        return f'Result is: {ex.exp3(float(num))}'
    elif user in ('root2', 'root3') and rt.root_check(num):
        if user == 'root2':
            return f'Result is: {rt.root2(float(num))}'
        return f'Result is: {rt.root3(float(num))}'
    elif user == 'fact' and f.fact_check(num):
        return f'Result is: {f.fact(int(num))}'
    elif user == 'log':
        num2 = input('Enter base number: ')
        if lgt.log_check(num2, num):
            return f'Result is: {lgt.log(float(num2), float(num))}'
        else:
            print('You entered invalid name of function.')
            return main()
    elif user in ('lg', 'ln') and lgt.log_check(b=float(num)):
        if user == 'lg':
            return f'Result is: {lgt.lg(float(num))}'
        return f'Result is: {lgt.lg(float(num))}'
    else:
        print('You entered invalid value')
        return main()


if __name__ == '__main__':
    print(main())
