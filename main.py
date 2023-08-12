import requests as req
from pyrogram import *
from Config import *
from Const import *





bot=Client('DrugLoad',
           api_id=API_ID,
           api_hash=API_HASH,
           bot_token=BOT_TOKEN)

def resul():
       url=basepoint+drug+endpoint
       res=req.get(url)
       drug_json=res.json()['results']
       purpose=str(drug_json[0]['purpose']).replace("['", "").replace("']", "")
       brand_name=str(drug_json[0]["openfda"]["brand_name"]).replace("['", "").replace("']", "")
       inactive_ingredient=str(drug_json[0]['inactive_ingredient']).replace("['", "").replace("']", "")
       active_ingredient=str(drug_json[0]['active_ingredient']).replace("['", "").replace("']", "")
       keep_out_of_reach_of_children=str(drug_json[0]['keep_out_of_reach_of_children']).replace("['", "").replace("']", "")
       warnings=str(drug_json[0]['warnings']).replace("['", "").replace("']", "")
       questions=str(drug_json[0]['questions']).replace("['", "").replace("']", "")
       spl_product_data_elements=str(drug_json[0]['spl_product_data_elements']).replace("['", "").replace("']", "")
       dosage_and_administration=str(drug_json[0]['dosage_and_administration']).replace("['", "").replace("']", "")
       manufacturer_name=str(drug_json[0]["openfda"]['manufacturer_name']).replace("['", "").replace("']", "")
       substance_name=str(drug_json[0]["openfda"]['substance_name']).replace("['", "").replace("']", "")
       generic_name=str(drug_json[0]["openfda"]['generic_name']).replace("['", "").replace("']", "")
       product_type=str(drug_json[0]["openfda"]['product_type']).replace("['", "").replace("']", "")
       product_ndc=str(drug_json[0]["openfda"]['product_ndc']).replace("['", "").replace("']", "")
       route=str(drug_json[0]["openfda"]['route']).replace("['", "").replace("']", "")
       storage_and_handling=str(drug_json[0]['storage_and_handling']).replace('["', "").replace('"]', "")
       package_label_principal_display_panel=str(drug_json[0]['package_label_principal_display_panel']).replace("['", "").replace("']", "")
       indications_and_usage=str(drug_json[0]['indications_and_usage']).replace("['", "").replace("']", "")
       global druginfo
       druginfo='General Name : '+generic_name+'\n\nBrand Name : '+brand_name+'\n\nManufacturer : '+manufacturer_name+'\n\nDrug Type : '+product_type+'\n\nRoute : '+route+'\n\nSubstance : '+substance_name+'\n\nNDC : '+product_ndc+'\n\nPackage Label : '+package_label_principal_display_panel
       global detailedinfo
       detailedinfo='Purpose : '+purpose+'\n\nSpl Elements : '+spl_product_data_elements+'\n\nActive Ingredients : '+active_ingredient+'\n\nInactive Ingredients : '+inactive_ingredient+'\n\nDosage & Usage : '+dosage_and_administration+'\n\nStorage & Handling : '+storage_and_handling+'\n\nIndications & Use : '+indications_and_usage
       global warns
       warns='Caution \n'+warnings+'\n\nKeep Out Of Children \n'+keep_out_of_reach_of_children+'\n\nQuestions\n'+questions

@bot.on_message(filters.command('start'))
async def strt_msg(client,message):
    await message.reply('**Hello '+message.from_user.first_name+"❤️**\n\nI'm __Drugload Bot💊__ developed by @rizad,I can retrieve drug data listed by Food and Drug Administration and fetch's the drug data you want.")
    
@bot.on_message(filters.command('about'))
async def strt_msg(client,message):
    await message.reply("Myself __Drugload Bot💊__ developed by @rizad,I can retrieve drug data listed by Food and Drug Administration and fetch's the drug data you want.if you have further queries chat with my developer")
    
@bot.on_message(filters.text)
async def druginfo(client,message):
    await message.reply('__Searching >> `'+message.text+'`__')
    global drug
    drug=message.text
    print(drug)
    try:
        resul()
        print(druginfo)
        await message.reply('<u>**General Details**</u>\n\n__'+druginfo+'__')
        await message.reply('<u>**Detailed Info**</u>\n\n__'+detailedinfo+'__')
        await message.reply('<u>**Warnings**</u>\n\n__'+warns+'__')
    except:
       await message.reply("__This Drug💉 Doesn't listed on Food and Drug Administration(FDA) or Spell it Correctly__")
bot.run()
