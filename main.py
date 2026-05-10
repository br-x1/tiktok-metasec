from metasec_4383 import Metasec

metasec = Metasec()

query_string = ""
x_ss_stub    = ""

x_sign = metasec.sign(query_string, x_ss_stub)

headers.update(x_sign)
