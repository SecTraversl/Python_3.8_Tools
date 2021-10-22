# %%
#######################################
def format_demo():
    """Prints multiple examples of format() syntax using many 'presentation types' as the 'format specifiers'; also includes the output of each line of code

    References:
        Format Specifiecation Mini-Language:  https://docs.python.org/3/library/string.html#formatspec
    """
    demo_string = """
    # STRING NOTATION - THIS DOES NOT CONVERT THE TYPE
    '{0:-^42s}'.format( 42 )
    # ValueError: Unknown format code 's' for object of type 'int'
    '{0:-^42s}'.format( '42' )
    # '--------------------42--------------------'
    '{0:-^42}'.format( '42' )
    # '--------------------42--------------------'
    str(42)
    # '42'  # this function converts the type, however


    # DECIMAL OR INTEGER NOTATION
    '{0:-^42d}'.format( 42 )
    # '--------------------42--------------------'
    '{0:-^42}'.format( 42 )
    # '--------------------42--------------------'


    # FLOAT NOTATION
    '{0:-^42f}'.format( 42 ) 
    # '----------------42.000000-----------------'
    '{0:-^42f}'.format( .42 ) 
    # '-----------------0.420000-----------------'


    # HEXADECIMAL - SMALL / LARGE LETTERS
    '{0:-^42x}'.format( 42 )
    # '--------------------2a--------------------'
    '{0:-^42x}'.format( 420 )
    # '-------------------1a4--------------------'
    '{0:-^42X}'.format( 42 )
    # '--------------------2A--------------------'
    '{0:-^42X}'.format( 420 )
    # '-------------------1A4--------------------'
    hex(420)
    # '0x1a4'
    int('0x1a4', 16)
    # 420


    # PERCENT NOTATION
    '{0:-^42%}'.format( 42 ) 
    # '---------------4200.000000%---------------'
    '{0:-^42%}'.format( .42 ) 
    # '----------------42.000000%----------------'


    # INTEGER TO CHARACTER CONVERSTION
    '{0:-^42c}'.format( 42 )
    # '--------------------*---------------------'
    '{0:-^42c}'.format( 420 )
    # '--------------------Ƥ---------------------'
    '{0:-^42c}'.format( 4200 )
    # '--------------------ၨ---------------------'
    chr(420)
    # 'Ƥ'
    ord('Ƥ')
    # 420


    # OCTAL NOTATION
    '{0:-^42o}'.format( 42 )
    # '--------------------52--------------------'
    '{0:-^42o}'.format( 420 )
    # '-------------------644--------------------'
    int('644', 8)
    # 420
    oct(420)
    # '0o644'


    # EXPONENTIAL NOTATION
    '{0:-^42e}'.format( 42 )
    # '---------------4.200000e+01---------------'
    '{0:-^42e}'.format( 4.2 )
    # '---------------4.200000e+00---------------'
    '{0:-^42e}'.format( 420 )
    # '---------------4.200000e+02---------------'


    # BINARY NOTATION
    '{0:-^42b}'.format( 42 )
    # '------------------101010------------------'
    '{0:-^42b}'.format( 420 )
    # '----------------110100100-----------------'
    int('110100100', 2)
    # 420
    bin(420)
    # '0b110100100'
    """
    print(demo_string)

