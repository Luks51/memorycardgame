===> Memory Card Game Instructions <===

> Aplikacija pisana i testirana u Python 3.9.7 verziji
> Preporučeno koristit veći zaslon 1920x1080 i scale 100% > pogledaj sliku u prilogu
> Potrebni library:
	> tkinter (najčešće po defaultu dolazi s Pythonom)
	> pillow / PIL (potrebna instalacija > cmd(admin) > pip install pillow)
	> ostali built-in
> Exportat repository u poseban folder
> Pokrenuti "Memory Card Game.py" datoteku direktno ili preko nekog IDE-a (testirano u Visual Studio Codeu i Python IDE-u)
> Spremno za igranje

> Objašnjenje: Memory card igra u kojoj imamo zadane levele s okrenutim karticama. Cilj igre je pronaći sve parove kartica
	Na početku igre nam se prikažu kartice s rješenjima na nekoliko sekundi te zatim mi moramo zapamtit mjesta što više
	parova kako bi nam kasnije bilo jednostavnije pronaći sve parove. Potrebno je koristiti mozak te logično razmišljat.
	Odlična igra za razvijanje pamćenja.

Početnim grafičkim sučeljem određujemo hoćemo li igrati, podesiti postavke, izađi iz igre:
	- Ako odaberemo igranje biramo između levela 1 i 2v2 moda. Rješavanjem levela slijedno otključavamo nove
	- Ako odaberemo postavke možemo prilagođavati težinu igre to jest duljinu prikaza kartica i težinu koja određuje duljinu
	  vremena levela
	- Ako izaberemo izlazak gasi se aplikacija
