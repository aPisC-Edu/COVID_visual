# Telepítéséi útmutató 

A WebIde-ben a workspace-re jobb gombbal kattintva előjön egy menü, ahol a git opció alatt 
a klónozást választva megadható ennek a repository-nak a címe (https://github.com/aPisC/COVID_visual.git).
Ezek után lemásolja az összes jelenlegi projekt file-t a repositoryból.
Utána a létrejött projektet kell buildelni (jobb kattintás / build). 
Elképzelhetőnek tartom, hogy fent fog akadni a build a megegyező schema nevek miatt, ha ilyen elő fordul, 
akkor a projekt főkönyvtárában lévő mta.yaml-fileban lehet módosítani (jobb katt / Open Code editor; 18.sor).

Ha sikeresen lefordult a projekt, akkor a Database Explorerben lehet csatlakoztatni és böngészni az adatokat. 
A nyers adatok a Tables/COVID_RAW táblában érhetőek el.
Az elkészült idősor a Views/COVIDTIMESERIES nézetben található.

Módosítottam a tábla és mezőneveken a legutóbbi emailem óta, de az adatok nem változtak, azt gondolom 
egyértelműen ki fognak derülni az új mező nevek a forrásokból és a Database Explorerből.

Csv fájlok és az importálás a db/src/data_source mappában, a táblák és nézetek definíciói a db/src/data mappában találhatóak.