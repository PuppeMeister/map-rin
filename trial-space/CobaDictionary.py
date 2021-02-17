import os.path

PSKS_client = {b'server1' : b'abcdef',
        b'server2' : b'uvwxyz'}

PSKS_server = {b'client1' : b'abcdef',
               b'client2' : b'123456'}

#b'value' : b'231.27#232.63#14.98#205.04#212.04'

PSKS_test = {
    b'kudalumping' : b'uvwxyz',
    b'kudalumping2' : b'abcdef',
    b'value' : b'231.27#232.63#14.98#205.04#212.04'}

_callback ={}
_callback_test ={}


#This is dictionary
psk={'psk_identity': b'my_psk_identity12345',
     'parameter': b',my_value_12345'}

def tuple_trial():
    test_tuple = ("abc", "efg")
    print("Type of test_tuple = ", type(test_tuple))
    test_tuple = test_tuple + ("hij", "klm")
    print(test_tuple)

def split_trial():

    print("---  Trial Split ---")
    bahan_di_split = "231.27#232.63#14.98#205.04#212.04*client_identity*abcdef"
    array_tampungan = bahan_di_split.split("*")
    print("Hasil array tampungan = ", array_tampungan)

def concate_dictionary_trial():

    print("--- Concate Trial ---")
    bahan_di_concate = {b'server1' : b'uvwxyz',
                        b'identity' : b'abcdef',
                        b'value' : b'231.27#232.63#14.98#205.04#212.04'}
    print("TYpe bahan_di_concate = ", type(bahan_di_concate))
    hasil_concate = bahan_di_concate[b'value'].decode("utf-8")+"*"+bahan_di_concate[b'identity'].decode("utf-8") +"*"+bahan_di_concate[b'server1'].decode("utf-8")

    print("Hasil = ", hasil_concate.encode())

if __name__ == '__main__':

    concate_dictionary_trial()
    #split_trial()
    #tuple_trial()
    """
    print("Trial Lambda")
    trial_lambda_client = lambda hint: (PSKS_client[hint], b'client1')
    trial_lambda_server = lambda identity: PSKS_server[identity]

    print("trial client = ", trial_lambda_client(b'server1'))
    print("trial server = ", trial_lambda_server(b'client1'))

    cb_server = trial_lambda_server if callable(trial_lambda_server) else lambda _identity: trial_lambda_server
    print("if trial_lamda_server is callable = ", callable(trial_lambda_server))

    print("Trial if isinstance(psk, tuple) else (psk, b"") = ", isinstance( trial_lambda_client, tuple))

    #cb_client = trial_lambda_client if callable(psk) else lambda _hint: psk if isinstance(psk, tuple) else (psk, b"")

    print("cb server = ", cb_server)

    ssl_id = 46043520
    _callback[ssl_id] =  trial_lambda_client;
    hint_from_server = b'server1'
    print("callback with client inside = ", _callback)
    print("callback with client inside with hint = ", _callback[ssl_id](hint_from_server))

    trial_lambda_test = lambda hint: (PSKS_test[hint], b'client1')
    _callback_test[ssl_id] = trial_lambda_test
    print("test = ", _callback_test[ssl_id](b'value'))
    """
