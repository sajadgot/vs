from pyrubi import Client
import re

auth = [{"auth":"iutoukkqpndluighxnojvqefclfjzjiu","key":"MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAJioPoABtgdBjCvqd3iilwkuL6NrQ0V/emcKtwZX1xDA4d543thgohN5r5MRdjcPpCXXajc40R9p2sZGCihj/50N4kD7qefn62C09F73mhj32t/c75B1xAKd71+E3DW+Q0m96lPSU79DCVFhpj2cUqa1XBMTT2Lf9Z17wl0bcXxvAgMBAAECgYAiti7wAHOZlsf+vGPKJH5fcgcXC67SQLhecctIP/UBNDqn0agqX167OvI3aMMOphnXGPJn+B1lHTbH2uk4YfSfMbqUoSXgqmfz6CBkbOLoELrt5CbAWqtfdITcAFnmaUArW1XaslmYPPcANXDY2NTlpBHAcTbAEWp/lnBmo4rkIQJBAMn5Q6UMdV3rtu1ny/zDmAEJMzwmuiQViTlM5y57hzDf9M8QE6do+IgMErx6pxwFKkQ0dB6co1RuT7Oz44HSt0kCQQDBfePiRVKmb7LZPP3ytOKvGOMrcQtX1hYrbGqS0JJ2Uu7C7CaIgLQiHC5RUa+NtOUdF3bGZdVcAIA8qsjUhH33AkEAuXua7cZFOt2v/tJl+Vk/DSR/0uvV4jGM9fx0CrIS84WY81fWVNYH+BjuU/1n3km4CS8KvNoo/O7ZbzTy6FS1UQJAUDX/4i0atiRX3/aIz7RsxGlswvV53k/BoP6wr2wHS0XV9LgwwSWZhwpnqQ5T2ErFL+oqMtTEPf93Ka8i0faawQJACIbB68MBj0XS0MDEHRN1AJRDbZGRjDjkQIGiiedRZM6NfM/YCW4XMAnphVlrvpv7G8sMhkCq8ILxYCuHr/18kg=="}]
for i in auth:
  bot = Client(auth=i["auth"], private=i["key"], platform="android")
  group_list = []  # تغییر نام list به group_list تا با نام پیش‌فرض Python تداخل نداشته باشد
  group_guid = "c0CBR4F0ad08f49e105097be3abc1a09"
  message_text = """"""
  link_pattern = r"https://rubika.ir/joing/\w{32}"
  
  def send_to_group(links):
      message = message_text + "\n".join(links)  # اضافه کردن پیشوند به هر لینک و ارسال در یک پیام
      bot.send_text(group_guid, message)
  
  message_links = []  # یک لیست برای اضافه کردن لینک‌ها تعریف می‌کنیم
  
  for msg in bot.on_message():
      try:
          if "https://rubika.ir/joing/" in msg.text:
              link = re.findall(link_pattern, msg.text)[0]
              if link not in message_links:  # اگر لینک در لیست نبود، اضافه کن
                  message_links.append(link)
          if len(message_links) == 35:  # اگر تعداد لینک‌ها به ۲۵ رسید
              send_to_group(message_links)  # لیست رو برای گروه فرستاده
              message_links = []  # لیست رو خالی کن برای لینک‌های بعدی
      except Exception as e:  # برای انجام خطاهندلینگ درست
          print("An exception occurred:", e)