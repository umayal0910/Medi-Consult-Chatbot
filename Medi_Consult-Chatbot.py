import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        speak("Good Afternoon!")   

    else:
        print("Good Evening!")
        speak("Good Evening!")  

    print("I am Medi-Consult. How may I help you!!")
    speak("I am Medi-Consult. How may I help you!!")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'acne' in query:
            print("If you have achne, then don't wash affected areas of skin more than twice a day. Frequent washing can irritate the skin and make symptoms worse.Wash the affected area with a mild soap or cleanser and lukewarm water. Very hot or cold water can make acne worse")
            speak("If you have achne, then don't wash affected areas of skin more than twice a day. Frequent washing can irritate the skin and make symptoms worse. Wash the affected area with a mild soap or cleanser and lukewarm water. Very hot or cold water can make acne worse")

        elif 'addisons Disease' in query:
            print("It is a disorder of the adrenal glands.The main symptoms of this disease are fatigue,muscle weakness,low mood,loss of apetite.The Method of treatment is daily medication.")
            speak("It is a disorder of the adrenal glands. The main symptoms of this disease are fatigue, muscle weakness, low mood, loss of apetite. The Method of treament is daily medication")
        
        elif 'alzheimer disease' in query:
            print("It is a neurological disease which affects multiple functions of the brain including memory.It may lead to severe head injuries and to conditions associated with cardivascular disease.Main symptoms are problems with speech and lanuguage,anxiety,difficulty in making decisions.You should undergo medication to relieve from some of the symptoms and slow down the progression of the condition in some people.")
            speak("It is a neurological disease which affects multiple functions of the brain including memory. It may lead to severe head injuries and to conditions associated with cardivascular disease. Main symptoms are problems with speech and lanuguage, anxiety, difficulty in making decisions. You should undergo medication to relieve from some of the symptoms and  slow down the progression of the condition in some people.")

        elif 'appendicitis' in query:
            print('It is a sweeling of appendix which is present in the large intestine.The main symptoms are severe pain in the abdomen region,diarrhoea and will feel sick.The treament method is only surgery,which may be an open surgery or laproscopy.')
            speak('It is a sweeling of appendix which is present in the large intestine. The main symptoms are severe pain in the abdomen region, diarrhoea and  will feel sick. The treament method is only surgery, which may be an open surgery or  laproscopy.')

        elif 'arthritis' in query:
            print('It is a common condition that causes pain and inflammation in a joint.Some of the symptoms are joint pain, inflammation in the joints and muscle weakness.The treatment method is medications like painkillers,non-steroidal anti-inflammatory drugs,corticosteroids and pysiotherapy.')
            speak('It is a common condition that causes pain and inflammation in a joint. Some of the symptoms are joint pain, inflammation in the joints and muscle weakness. The treatment method is medications like painkillers, non-steroidal anti-inflammatory drugs, corticosteroids and  pysiotherapy')
        
        elif 'asthma' in query:
            print('It is due to inflammation of the bronchi.The symptoms are coughing, wheezing, chest tightness and breathlessness.The treament is relieving symptoms preventing future symptoms and attacks.Inhalers allows the airways to open wider, making it easier to breathe again.')
            speak('It is due to inflammation of the bronchi. The symptoms are coughing, wheezing, chest tightness and breathlessness. The treament is relieving symptoms preventing future symptoms and attacks. Inhalers allows the airways to open wider, making it easier to breathe again.')

        elif 'bileduct cancer' in query:
            print("Bile duct is present in the digestive system uses to help break down fats and digest foods.Symptoms of bileduct cancer is jaundice,abdominal pain,weight loss.The way of treatment is Cancer of the bile duct can usually only be cured if cancerous cells haven't spread,if this is the case, some or all of the bile duct may be removed.")
            speak("Bile duct is present in the digestive system uses to help break down fats and digest foods. Symptoms of bileduct cancer is jaundice, abdominal pain, weight loss. The way of treatment is Cancer of the bile duct can usually only be cured if cancerous cells haven't spread, if this is the case, some or all of the bile duct may be removed.")
        
        elif 'bone cancer' in query:
            print('Bone cancer can affect any bone, but most cases develop in the long bones of the legs or upper arms.The main symptoms include persistent bone pain that gets worse,swelling and redness (inflammation) over a bone,a weak bone that breaks (fractures) more easily than normal.The treatment method may be chemotherapy,radiotherapy,surgery to remove the section of cancerous bone.')
            speak('Bone cancer can affect any bone, but most cases develop in the long bones of the legs or upper arms. The main symptoms include persistent bone pain that gets worse,swelling and redness (inflammation) over a bone,a weak bone that breaks (fractures) more easily than normal. The treatment method may be chemotherapy, radiotherapy, surgery to remove the section of cancerous bone.')
        
        elif 'brain tumour' in query:
            print('A brain tumour is a growth of cells in the brain that multiplies in an abnormal, uncontrollable way. It can either be cancerous (malignant) or non-cancerous (benign).Some of the symptoms may be severe headaches,persistent nausea,vomiting and drowsiness,paralysis of the body.The main treatment for most brain tumours is surgery, which aims to remove as much of the abnormal tissue as possible or chemotherapy.')
            speak('A brain tumour is a growth of cells in the brain that multiplies in an abnormal, uncontrollable way. It can either be cancerous (malignant) or non-cancerous (benign). Some of the symptoms may be severe headaches, persistent nausea,vomiting and drowsiness, paralysis of the body. The main treatment for most brain tumours is surgery, which aims to remove as much of the abnormal tissue as possibleor chemotherapy.')

        elif 'bronchithis' in query:
            print('Bronchitis is an infection of the main airways of the lungs (bronchi), causing them to become irritated and inflamed.The main symptom is a cough,sore throat and wheezing.There is no specific treatment for bronchitis but the individual should undergo medication to slow down the effects.')
            speak('Bronchitis is an infection of the main airways of the lungs (bronchi), causing them to become irritated and inflamed. The main symptom is a cough, sore throat and wheezing.There is no specific treatment for bronchitis but the individual should undergo medication to slow down the effects.')

        elif 'chest pain' in query:
            speak('Chest pain can be caused by anything from muscle pain to a heart attack which may be because of the block in the path of blood circulation and should never be ignored.Some symptoms are breathlessness, nausea, sweating, or coughing up blood.The treatment is medication and surgery.')
            print('Chest pain can be caused by anything from muscle pain to a heart attack which may be because of the block in the path of blood circulation and should never be ignored. Some symptoms are breathlessness, nausea, sweating, or coughing up blood.The treatment is medication and surgery.')

        elif 'chickenpox' in query:
            print('It causes a rash of red, itchy spots that turn into fluid-filled blisters. They then crust over to form scabs, which eventually drop off.The main symptoms are feeling sick,high temperature,loss of appetite.The treatment include paracetamol to relieve fever, and calamine lotion and cooling gels to ease itching.')
            speak('It causes a rash of red, itchy spots that turn into fluid-filled blisters. They then crust over to form scabs, which eventually drop off. The main symptoms are feeling sick, high temperature, loss of appetite. The treatment include paracetamol to relieve fever, and calamine lotion and cooling gels to ease itching.')

        elif 'chronic pancreatitis' in query:
            print("It is a condition where the pancreas becomed permenantly damaged from inflammation.The main symptoms are nausea,vomiting, and abdominal pain.Surgery is sometimes needed to treat severe chronic pain that doesn't respond to painkillers.")
            speak("It is a condition where the pancreas becomed permenantly damaged from inflammation. The main symptoms are nausea, vomiting and abdominal pain. Surgery is sometimes needed to treat severe chronic pain that doesn't respond to painkillers.")

        elif 'cough' in query:
            print('A cough is a reflex action to clear your airways of mucus and irritants such as dust or smoke.Some of the treatments is syrups like benadryl,cofsils and some tablets.')
            speak('A cough is a reflex action to clear your airways of mucus and irritants such as dust or smoke. Some of the treatments is syrups like benadryl, cofsils and some tablets.')

        elif 'coronavirus' in query:
            print('It is a dreadful disease.The major symptoms are cough,cold,high fever,and severe pains in the body.The treatment is the vaccine covi-shield19 which is even not a permanent cure.')
            speak('It is a dreadful disease. The major symptoms are cough, cold, high fever and severe pains in the body. The treatment is the vaccine covi-shield19 which is even not a permanent cure.')

        elif 'dermatitis' in query:
            print('It is a type of skin disease.Symptoms are severe itching and often stinging.The treatment is applying ointments,gel to the affected part of your skin.')
            speak('It is a type of skin disease. Symptoms are severe itching and often stinging. The treatment is applying ointments, gel to the affected part of your skin.')

        elif 'diabetes' in query:
            print("Diabetes is a lifelong condition that causes a person's blood glucose (sugar) level to become too high.The main symptoms are weight loss,feeling very tired,feeling very thirsty and dizzy.The main treatment is medication and intake of the drug insulin in the form of syringe.")
            speak("Diabetes is a lifelong condition that causes a person's blood glucose (sugar)level to become too high. The main symptoms are weight loss, feeling very tired, feeling very thirsty and dizzy. The main treatment is medication and intake of the drug insulin in the form of syringe.")
            
        elif 'diarrhoea' in query:
            print('Diarrhoea is passing looser or more frequent stools than is normal for you.You can take loperamide during diarrhoea.')
            speak('Diarrhoea is passing looser or more frequent stools than is normal for you. You can take loperamide during diarrhoea.')

        elif 'epilepsy' in query:
            print('Epilepsy is a condition that affects the brain and causes repeated seizures,which is brusting up of neurons by firing off the electrical impulses.It can be caused by stroke,brain tumours.The treatment is with medications called anti-epileptic drugs ,these medications cannot cure epilepsy, but they are often very effective in controlling seizures.')
            speak('Epilepsy is a condition that affects the brain and causes repeated seizures,which is brusting up of neurons by firing off the electrical impulses. It can be caused by stroke, brain tumours. The treatment is with medications called anti-epileptic drugs ,these medications cannot cure epilepsy, but they are often very effective in controlling seizures.')
        
        elif 'eye cancer' in query:
            print('It is the ocular cancer.Some symptoms maybe blurred vision,pain around the eye,shadows,flases of light in your vision.The main treatments are branchytherapy,external radiotherapy or surgery to remove the tumour part of the eye, or chemotherapy.')
            speak('It is the ocular cancer. Some symptoms maybe blurred vision,pain around the eye, shadows, flases of light in your vision. The main treatments are branchytherapy, external radiotherapy or surgery to remove the tumour part of the eye, or chemotherapy.')
        
        elif 'fever' in query:
            print('It is just a small illness.The symptoms is high temperature.The treatment is taking tablets like calpol,dolo 650.')
            speak('It is just a small illness. The symptoms is high temperature. The treatment is taking tablets like calpol, dolo 650.')

        elif 'flu' in query:
            print('Flu (influenza) is a common infectious viral illness spread by coughs and sneezes.The main symptoms of flu is include high temperature above 34C,headache,general aches and dry cough.The treatments are always wash your hands regularly with soap and warm water,use tissues to cover your mouth and nose when you cough or sneeze.')
            speak('Flu (influenza) is a common infectious viral illness spread by coughs and sneezes. The main symptoms of flu is include high temperature above 34C, headache, general aches and dry cough.The treatments are always wash your hands regularly with soap and warm water,use tissues to cover your mouth and nose when you cough or sneeze.')

        elif 'food poisoning' in query:
            print('Food poisoning is an illness caused by eating contaminated food.The main symptoms include feeling sick (nausea),vomiting,diarrhoea.The remedies are practice good hygiene,clean food preparation places.')
            speak('Food poisoning is an illness caused by eating contaminated food. The main symptoms include feeling sick (nausea), vomiting, diarrhoea.The remedies are practice good hygiene, clean food preparation places.')

        elif 'headache' in query:
            print('They feel like a constant ache that affects both sides of the head, as though a tight band is stretched around it.You can take the tablet paracetamol.')
            speak('They feel like a constant ache that affects both sides of the head, as though a tight band is stretched around it. You can take the tablet paracetamol.')

        elif 'hiv' in query:
            print('HIV stands for human immunodeficiency virus. The virus targets the immune system and if untreated, weakens your ability to fight infections and disease.Treatments for HIV are now very effective, enabling people with HIV to live long and healthy lives.Medication, known as antiretrovirals, work by stopping the virus replicating in the body, allowing the immune system to repair itself and preventing further damage.')
            speak('HIV stands for human immunodeficiency virus. The virus targets the immune system and if untreated, weakens your ability to fight infections and disease. Treatments for HIV are now very effective, enabling people with HIV to live long and healthy lives. Medication, known as antiretrovirals, work by stopping the virus replicating in the body, allowing the immune system to repair itself and preventing further damage.')

        elif 'kidney stones' in query:
            print('Kidney stones can develop in one or both kidneys and most often affect people aged 30 to 60.The waste products in the blood can occasionally form crystals that collect inside the kidneys. Over time, the crystals may build up to form a hard stone.Most kidney stones are small enough to be passed in your urine, and it may be possible to treat the symptoms at home with medication.Larger stones may need to be broken up using ultrasound or laser energy.')
            speak('Kidney stones can develop in one or both kidneys and most often affect people aged 30 to 60. The waste products in the blood can occasionally form crystals that collect inside the kidneys. Over time, the crystals may build up to form a hard stone.Most kidney stones are small enough to be passed in your urine, and it may be possible to treat the symptoms at home with medication. Larger stones may need to be broken up using ultrasound or laser energy.')

        elif 'liver cancer' in query:
            print('Symptoms of liver cancer are unexplained weight loss,loss of appetite,vomiting pain or swelling in your abdomen,jaundice,itchy skin.Treatment options in the early stages of liver cancer include surgery to remove a section of liver,liver transplant,microwave or radiofrequency ablation – where microwaves or radio waves are used to destroy the cancerous cells')
            speak('Symptoms of liver cancer are unexplained weight loss, loss of appetite, vomiting pain or swelling in your abdomen, jaundice, itchy skin. Treatment options in the early stages of liver cancer include surgery to remove a section of liver, liver transplant, microwave or radiofrequency ablation – where microwaves or radio waves are used to destroy the cancerous cells')

        elif 'lung cancer' in query:
            print('Symptoms includes  persistent cough,coughing up blood,persistent breathlessness,tiredness and weight loss,pain when breathing or coughing.Treatment is due to the severity of the health effects,if general then radiotherapy ,else chemotheraphy in case of severe effects.')
            speak('Symptoms includes  persistent cough,coughing up blood, persistent breathlessness, tiredness and weight loss, pain when breathing or coughing. Treatment is due to the severity of the health effects,if general then radiotherapy ,else chemotheraphy in case of severe effects.')
          
        elif 'malaria' in query:
            print("Malaria is a serious tropical disease spread by mosquitoes. If it isn't diagnosed and treated promptly, it can be fatal.A single mosquito bite is all it takes for someone to become infected.Symptoms include high temperature (fever),sweats and chills,headaches,vomiting,muscle pains,diarrhoea.Antimalarial medication is used to both treat and prevent malaria,which type of medication is used and the length of treatment will depend on the type of malaria, and the severity of your symptoms")
            speak("Malaria is a serious tropical disease spread by mosquitoes. If it isn't diagnosed and treated promptly, it can be fatal. A single mosquito bite is all it takes for someone to become infected. Symptoms include high temperature (fever), sweats and chills, headaches, vomiting, muscle pains, diarrhoea. Antimalarial medication is used to both treat and prevent malaria, which type of medication is used and the length of treatment will depend on the type of malaria, and the severity of your symptoms")
            
        elif 'meningitis' in query:
            print('Meningitis is an infection of the protective membranes that surround the brain and spinal cord (meninges).Symptoms of meningitis develop suddenly and can include a high temperature,being sick,a headache,stiff neck,a dislike of bright lights,drowsiness,seizures (fits).People with suspected meningitis will usually have tests in hospital to confirm the diagnosis and check whether the condition is the result of a viral or bacterial infection.Bacterial meningitis usually needs to be treated in hospital for at least a week. Treatments include antibiotics given directly into a vein,fluids given directly into a vein,oxygen through a face mask')
            speak('Meningitis is an infection of the protective membranes that surround the brain and spinal cord (meninges). Symptoms of meningitis develop suddenly and can include a high temperature,  being sick,  a headache,  stiff neck, a dislike of bright lights, drowsiness, seizures (fits). People with suspected meningitis will usually have tests in hospital to confirm the diagnosis and check whether the condition is the result of a viral or  bacterial infection.  Bacterial meningitis usually needs to be treated in hospital for at least a week. Treatments include antibiotics given directly into a vein,  fluids given directly into a vein, oxygen through a face mask')

        elif 'pancreatic cancer' in query:
            print('Pancreatic cancer is caused by the abnormal and uncontrolled growth of cells in the pancreas.Symptoms of pancreatic cancer include nausea and vomiting,bowel changes,fever and shivering,indigestion,blood clots.The three main treatments for pancreatic cancer are surgery,chemotherapy,radiotherapy')
            speak('Pancreatic cancer is caused by the abnormal and uncontrolled growth of cells in the pancreas. Symptoms of pancreatic cancer include nausea and vomiting, bowel changes, fever and shivering, indigestion, blood clots. The three main treatments for pancreatic cancer are surgery, chemotherapy, radiotherapy')

        elif 'parkinson disease' in query:
            print("Parkinson's disease is a condition in which parts of the brain become progressively damaged over many years.The three main symptoms of Parkinson's disease are involuntary shaking of particular parts of the body,slow movement,stiff and inflexible muscles.The treatments include supportive treatments – such as physiotherapy and occupational therapy,medication,in some cases, brain surgery")
            speak("Parkinson's disease is a condition in which parts of the brain become progressively damaged over many years.The three main symptoms of Parkinson's disease are involuntary shaking of particular parts of the body, slow movement, stiff and inflexible muscles.The treatments include supportive treatments – such as physiotherapy and occupational therapy,medication,in some cases, brain surgery.")

        elif 'pneumonia' in query:
            print("Pneumonia is swelling (inflammation) of the tissue in one or both lungs. It's usually caused by a bacterial infection.Some symptoms include cough,rapid heartbeat,fever,loss of appetite,fatigue.Mild pneumonia can usually be treated at home by getting plenty of rest,taking antibiotics, and drinking plenty of fluids")
            speak("Pneumonia is swelling (inflammation) of the tissue in one or both lungs. It's usually caused by a bacterial infection.Some symptoms include cough, rapid heartbeat, fever, loss of appetite, fatigue. Mild pneumonia can usually be treated at home by getting plenty of rest, taking antibiotics, and drinking plenty of fluids")

        elif 'retinoblastoma' in query:
            print('Retinoblastoma is a rare type of eye cancer that can affect young children.Symptoms include unusual reflection in the pupil,red or inflamated eye,poor vision.This can be treated as intraocular – where the cancer is completely within the eye ,extraocular – where the cancer spreads beyond the eye to the surrounding tissue, or to another part of the body')
            speak('Retinoblastoma is a rare type of eye cancer that can affect young children. Symptoms include unusual reflection in the pupil,red or inflamated eye,poor vision. This can be treated as intraocular – where the cancer is completely within the eye ,extraocular – where the cancer spreads beyond the eye to the surrounding tissue, or to another part of the body')

        elif 'sickle cell anemia' in query:
            print('Sickle cell disease affects how your body produces red blood cells. Normal red blood cells are round – red blood cells affected by sickle cell disease harden and become sickle-shaped, like a crescent moon. This causes them to die too quickly and block blood vessels, leading to symptoms that are often painful.Painkillers like paracetamol and ibuprofen can help, warm towels can be placed on the area and massaged to ease the pain, and must drink plenty of water.')
            speak('Sickle cell disease affects how your body produces red blood cells. Normal red blood cells are round – red blood cells affected by sickle cell disease harden and become sickle-shaped, like a crescent moon. This causes them to die too quickly and block blood vessels, leading to symptoms that are often painful. Painkillers like paracetamol and ibuprofen can help, warm towels can be placed on the area and massaged to ease the pain, and must drink plenty of water.')

        elif 'skin cancer' in query:
            print('Skin cancer is one of the most common cancers in the world which refers to a group of cancers that slowly develop in the upper layers of the skin.The symptoms are due to the exposure of UV rays.Surgery is the main treatment for skin cancer. This involves removing the cancerous tumour and some of the surrounding skin')
            speak('Skin cancer is one of the most common cancers in the world which refers to a group of cancers that slowly develop in the upper layers of the skin. The symptoms are due to the exposure of UV rays. Surgery is the main treatment for skin cancer. This involves removing the cancerous tumour and some of the surrounding skin')
        
        elif 'stomach cancer' in query:
            print("Stomach cancer, or gastric cancer, is a fairly uncommon type of cancer.The major symptoms are indigestion,heartburn,stomach pain.Many cases of stomach cancer can't be completely cured, but it's still possible to relieve symptoms and improve quality of life using chemotherapy and in some cases radiotherapy and surgery")
            speak("Stomach cancer, or gastric cancer, is a fairly uncommon type of cancer. The major symptoms are indigestion,heartburn,stomach pain. Many cases of stomach cancer can't be completely cured, but it's still possible to relieve symptoms and improve quality of life using chemotherapy and in some cases radiotherapy and surgery")

        elif 'ulcer' in query:
            print("That are develop on the lining of the stomach. Ulcers can also occur in part of the intestine just beyond the stomach. These are called duodenal ulcers.Symptoms may be indigestion,heartburn,nausea (feeling sick).You'll be treated using antibiotics if your ulcer was caused by a H. pylori infection. This kills the bacteria and should prevent the ulcer coming back.")
            speak("That are develop on the lining of the stomach. Ulcers can also occur in part of the intestine just beyond the stomach. These are called duodenal ulcers. Symptoms may be indigestion, heartburn, nausea (feeling sick). You'll be treated using antibiotics if your ulcer was caused by a H. pylori infection. This kills the bacteria and should prevent the ulcer coming back.")

        elif 'stroke' in query:
            print("A stroke is a serious, life-threatening medical condition that occurs when the blood supply to part of the brain is cut off.There maybe no movements in the face,arms,even can't speak.The specific treatments recommended depend on whether a stroke is caused by blood clot obstructing the flow of blood to the brain ,bleeding in or around the brain (haemorrhagic stroke)")
            speak("A stroke is a serious, life-threatening medical condition that occurs when the blood supply to part of the brain is cut off. There maybe no movements in the face, arms, even can't speak. The specific treatments recommended depend on whether a stroke is caused by blood clot obstructing the flow of blood to the brain (ischaemic stroke), bleeding in or around the brain (haemorrhagic stroke)")

        elif 'thyroid cancer' in query:
            print('Thyroid cancer is a rare type of cancer that affects the thyroid gland, a small gland at the base of the neck.The most common symptom of cancer of the thyroid is a painless lump or swelling that develops in the neck.Differentiated thyroid cancers (DTCs) are treated using a combination of surgery to remove the thyroid gland (thyroidectomy) and a type of radiotherapy that destroys any remaining cancer cells and prevents the thyroid cancer returning.')
            speak('Thyroid cancer is a rare type of cancer that affects the thyroid gland, a small gland at the base of the neck.The most common symptom of cancer of the thyroid is a painless lump or swelling that develops in the neck. Differentiated thyroid cancers (DTCs) are treated using a combination of surgery to remove the thyroid gland (thyroidectomy) and a type of radiotherapy that destroys any remaining cancer cells and prevents the thyroid cancer returning.')

        elif 'tooth decay' in query:
            print('Tooth decay can occur when acid is produced from plaque, which builds up on your teeth.If plaque is allowed to build up, it can lead to further problems, such as dental caries (holes in the teeth), gum disease or dental abscesses.Symptoms are toothache,tooth sensitivity,bad breath.Treatment of tooth decay depends on how advanced it is,they may apply a fluoride gel, varnish or paste to the area, removing the dental decay, offering local anaesthetic to numb the tooth and filling the hole,a process known as root canal treatment.')
            speak('Tooth decay can occur when acid is produced from plaque, which builds up on your teeth. If plaque is allowed to build up, it can lead to further problems, such as dental caries (holes in the teeth), gum disease or dental abscesses. Symptoms are toothache,tooth sensitivity,bad breath. Treatment of tooth decay depends on how advanced it is, they may apply a fluoride gel, varnish or paste to the area, removing the dental decay, offering local anaesthetic to numb the tooth and filling the hole,a process known as root canal treatment.')

        elif 'tuberculosis' in query:
            print('Tuberculosis (TB) is a bacterial infection spread through inhaling tiny droplets from the coughs or sneezes of an infected person.Typical symptoms of TB include persistent cough that lasts more than three weeks,weight loss,night sweats,high temperature (fever).Several different antibiotics are used. This is because some forms of TB are resistant to certain antibiotics. If you are infected with a drug-resistant form of TB, treatment with six or more different medications may be needed.')
            speak('Tuberculosis (TB) is a bacterial infection spread through inhaling tiny droplets from the coughs or sneezes of an infected person. Typical symptoms of TB include persistent cough that lasts more than three weeks, weight loss, night sweats, high temperature (fever).Several different antibiotics are used. This is because some forms of TB are resistant to certain antibiotics. If you are infected with a drug-resistant form of TB, treatment with six or more different medications may be needed.')

        elif 'whooping cough' in query:
            print('Whooping cough, also called pertussis, is a highly contagious bacterial infection of the lungs and airways.The symptoms of whooping cough are similar to those of a cold, such as a runny nose, red and watery eyes, a sore throat, and a slightly raised temperature.The treatment is medical treatment for children,antibiotics and paracetamol,ibuprofen for fever.')
            speak('Whooping cough, also called pertussis, is a highly contagious bacterial infection of the lungs and airways. The symptoms of whooping cough are similar to those of a cold, such as a runny nose, red and watery eyes, a sore throat, and a slightly raised temperature. The treatment is medical treatment for children,antibiotics and paracetamol,ibuprofen for fever.')

        elif 'yellow fever' in query:
            print('Yellow fever is a serious viral infection that is spread by certain types of mosquito.The symptoms of yellow fever occur in two stages. The initial symptoms develop three to six days after infection, and can include high temperature (fever),a headache,nausea or vomiting,muscle pain, including backache loss of appetite.There is no specific treatments for yellow fever hence we can use vaccine which protects you from infection when you travel to a country where yellow fever virus occurs and prevents the disease from spreading between countries.')
            speak('Yellow fever is a serious viral infection that is spread by certain types of mosquito. The symptoms of yellow fever occur in two stages. The initial symptoms develop three to six days after infection, and can include high temperature (fever),a headache, nausea or vomiting, muscle pain, including backache loss of appetite. There is no specific treatments for yellow fever hence we can use vaccine which protects you from infection when you travel to a country where yellow fever virus occurs and prevents the disease from spreading between countries.')

        elif 'quit' in query:
            print("Quitting the program. Thank you!!!")
            speak("Quitting the program. Thank you!!!")
            quit()

        else:
            print("Sorry,I don't understand,but we will surely get to know about that")
            speak("Sorry,I don't understand,but we will surely get to know about that")