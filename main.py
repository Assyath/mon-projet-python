import os
import asyncio
import base64
from dotenv import load_dotenv
from rodiumai import RodiumAI, client

# Charger la clé API depuis le fichier .env
load_dotenv()
api_key = os.getenv("RODIUMAI_API_KEY")

if not api_key:
    print("Erreur : Cle API manquante dans le fichier .env.")
    exit(1)

async def main():
    # Initialisation du client 
    client = RodiumAI()
    
    # Variable de navigation
    etape = 1
    print("=== SCRIPT INTERACTIF RODIUMAI VERSION SDK ===")

    while 1 <= etape <= 3:

    
        # ETAPE 1 : CHAT
        
        if etape == 1:
            print("\n=== Etape 1 : Chat ===")
            votre_question = input("Votre question : ")
            
            print("Envoi de la question via le SDK...")
            try:
                
                rep = await client.model("openai/gpt-4o-mini").temperature(0.7).chat(votre_question)
                
                
                texte_reponse = rep.choices[0].message.content
                cout_rodi = getattr(rep, "cost_rodi", "Non specifie")
                
                print(f"\n[reponse du modele]\n{texte_reponse}")
                print(f"Cout : {cout_rodi} RODI")
                
            except Exception as e:
                print(f"Erreur lors du chat : {e}")
                
            print("")
            choix = input("Rester (r) ou passer a la suivante (s) ? ").lower()
            if choix == 's':
                etape = 2

        # ETAPE 2 : IMAGE 
       
        elif etape == 2:
            print("\n=== Etape 2 : Image ===")
            description_image = input("Decrivez l'image : ")
            
            print("Generation de l'image via le SDK...")
            try:
                
                rep_image = await client.images.generate(
                    model="google/gemini-3.1-flash-lite-image",
                    prompt=description_image,
                    n=1,
                    size="1024x1536",
                    quality="medium"
                )
                
            
                if hasattr(rep_image, "data") and isinstance(rep_image.data, list):
                    base64_data = rep_image.data[0].b64_json
                elif hasattr(rep_image, "data"):
                    base64_data = getattr(rep_image.data, "b64_json", None)
                else:
                    base64_data = rep_image.get("data", [{}])[0].get("b64_json")
                
                if base64_data:
                    with open("image.png", "wb") as f:
                        f.write(base64.b64decode(base64_data))
                    print("Image enregistree avec succes : image.png")
                else:
                    print("Erreur : Impossible d'extraire le format Base64.")
                    raise Exception("Format inconnu")
                    
            except Exception as e:
                print(f"Erreur lors de la generation de l'image : {e}")
                                                      
                print("")
            choix = input("Revenir (b), rester (r) ou passer a la suivante (s) ? ").lower()
            if choix == 'b':
                etape = 1
            elif choix == 's':
                etape = 3

                
        # ETAPE 3 : VIDEO
        elif etape == 3:
            print("\n=== Etape 3 : Video ===")
            description_video = input("Decrivez la video : ")
            
            print("Generation de la video via le SDK...")
            try:
                
                rep_video = await client.video(
                    model="google/veo-3.1-lite",
                    prompt=description_video,
                    duration_seconds=4,
                    aspect_ratio="9:16"
                )
                
                if hasattr(rep_video, "data") and isinstance(rep_video.data, list):
                    base64_video = rep_video.data[0].b64_json
                else:
                    base64_video = rep_video.data.b64_json
                    
                with open("video.mp4", "wb") as f:
                    f.write(base64.b64decode(base64_video))
                print("Video enregistree avec succes : video.mp4")
            
            except Exception as e:
                print(f"Erreur lors de la generation de la video : {e}")
                                          
                print("")
            choix = input("Revenir (b), rester (r) ou quitter (q) ? ").lower()
            if choix == 'b':
                etape = 2
            elif choix == 'q':
                print("\nFin du programme. Au revoir !")
                break


# 3. Lancement du programme de maniere asynchrone
if __name__ == "__main__":
    asyncio.run(main())
