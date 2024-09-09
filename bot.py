import discord
from discord.ext import commands
import requests


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command('mem')
async def mem(ctx):
    with open('', 'rb') as f:
        picture = discord.File(f) 
    await ctx.send(file =picture)

    
def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await(ctx).send(image_url)


@bot.command()
async def atik(ctx, *, atik_turu):
    atik_turu = atik_turu.lower()

    if "plastik" in atik_turu:
        await ctx.send(
            "Plastik atıkları geri dönüşüm kutusuna atabilirsiniz. Ancak plastik poşetler, ince plastikler ve plastik oyuncaklar genellikle geri dönüştürülemez. "
            "Lütfen geri dönüştürülebilir sembolüne dikkat edin!"
        )
    elif "cam" in atik_turu:
        await ctx.send(
            "Cam şişeleri ve kavanozları geri dönüşüm kutusuna atabilirsiniz. Fakat kırık camlar, ampuller ve aynalar geri dönüştürülemez."
            
        )
        await ctx.send(file =picture)

        with open('', 'rb') as f:
            picture = discord.File(f) 

    elif "kağıt" in atik_turu:
        await ctx.send(
            "Kağıt ve karton atıklarını geri dönüşüm kutusuna atabilirsiniz. Islanmış veya yağlanmış kağıtlar geri dönüştürülemez."
        )
    elif "NedenGeriDönüşümYapmalıyız?" in atik_turu:
        await ctx.send(
            "Geri dönüşüm yapmanın hem doğal çevre hem de bizim için sayısız önemi vardır. Örnek vermek gerekirse kullanılmış kağıdın geri dönüşümü hava kirliliğini %74-94, su kirliliğini %35, su kullanımını %45 azaltır. 1 ton atık kağıdın kağıt hamuruna katılması 8 ağacın kesilmesini önlemektedir.. Herkesin geri dönüşüm yapmaya davet etmeli herkesi geri dönüşüm konusunda bilgilendirmeliyiz."
        )
    elif "organik" in atik_turu or "yemek" in atik_turu:
        await ctx.send(
            "Organik atıkları kompost yapabilirsiniz. Sebze, meyve kabukları, kahve telvesi gibi atıklar komposta uygundur. "
            "Ancak et ve süt ürünlerini komposta eklememelisiniz."


        )
    elif "metal" in atik_turu:
        await ctx.send(
            "Alüminyum kutular, teneke kutular gibi metal atıkları geri dönüşüm kutusuna atabilirsiniz. "
            "Ancak boya kutuları ve kimyasal içeren metaller geri dönüştürülemez."
        )
    else:
        await ctx.send("Bu atık türü için henüz bir bilgi yok. Lütfen yaygın atık türlerini kullanın: plastik, cam, kağıt, organik, metal.")


bot.run('')
