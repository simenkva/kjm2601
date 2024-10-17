# Tetthetsfunksjonalteori

Dette notatet er en kort introduksjon til tetthetsfunksjonalteori, eller "density-functional theory" (DFT) på engelsk. **Tetthetsfunksjonalteori er kvantekjemiens ubestridte arbeidshest.** De aller fleste beregninger i kjemi gjort i dag er med DFT. Grunnen er at det er den eneste metoden som kan brukes med dagens datamaskiner og samtidig regne ut noenlunde nøyaktige egenskaper for molekyler av interessant størrelse. DFT er mer nøyaktig enn Hartree-Fock, mens kostnadene er omtrent de samme.

***NB:*** DFT er pensum. Dette notatet er ment som en orientering og generell beskrivelse, og det ikke meningen at du skal kunne gjenta utledningene her. De er uansett ikke helt presise, og mange tekniske steg er forbigått. Det viktigste er at DFT kan ses på som en korreksjon til Hartree--Fock, og at Kohn--Sham-likningene har samme struktur som Hartree--Fock. Det er viktig å opparbeide seg en viss forståelse for hvordan Kohn-Sham-likningene er bygget opp, og hva det teoretiske grunnlaget for DFT er.

## Walther Kohn

I 1999 fikk Walther Kohn nobelprisen for oppfinnelsen av DFT. (Prisen ble delt med John Pople som fikk pris for sitt bidrag til kvantekjemi.) Han var en Østerriksk-Amerikansk jødisk fysiker, som ble reddet fra Østerrike til England av de allierte rett etter at Hitler hadde annektert landet, i 1938-1939. Han ble fraktet til Toronto i Canada. Han fikk ikke lov å studere kjemi siden han var tysk, og studerte derfor fysikk og matematikk. Likevel fikk han i 1998 nobelprisen i kjemi for sitt arbeid med DFT! Han tok PhD ved Harvard i USA, og ble professor ved University of California at Santa Barbara. 

![[walther-kohn.png|300]]


## Hohenberg-Kohn-teoremet og dets konsekvenser

### Schrödingerlikninga, en påminnelse 

For et gitt molekylært system har vi et ytre kjernepotensial
$$
	V_{\text{nuc}}(\mathbf{r}) = \sum_{a=1}^{N_{\text{atom}}} \frac{-Z_a e^2}{4\pi\varepsilon_0 |\mathbf{r} - \mathbf{R}_a|}.
$$
Her er $\mathbf{R}_a$ kjerneposisjon til atom nummer $a$, og $Z_a$ er kjerneladningen i enheter av $-e$. 

Vi søker grunntilstanden Det vil si at vi har en løsning av Schrødingerlikningen med minst energi $E$:
$$
	[T_e + V_{ee} + V_{\text{nuc}}]\Psi = E \Psi.
$$
Ekvivalent ønsker vi å minimere forventningsverdien til energien over alle normerte bølgefunksjoner. (Variasjonsprinsippet/metoden.)
$$ 
E_0 = \min_{\Psi} \braket{\Psi|T_e + V_{ee} + V_\text{nuc}|\Psi}
$$
Vi bemerker at bølgefunksjonen $\Psi(1,2,\ldots,N)$ er en *svært komplisert funksjon* og at vi er motivert til å vinne en enklere beskrivelse.

### Elektrontettheten

Hohenberg-Kohn-teoremet er en bemerkelsesverdig observasjon som omhandler *elektrontettheten*, en av de viktigste observablene. Vi definerer **tettheten** $\rho(\mathbf{r})$ assosiert med en $N$-elektron-bølgefunksjon: Tettheten er $N$ ganger sannsynligheten for å finne minst ett elektron i posisjonen $\mathbf{r}$.  Formelen er
$$
	\rho(\mathbf{r}) = N \int d\mathbf{r}_2 \cdots d\mathbf{r}_N |\Psi(\mathbf{r},\mathbf{r}_2,\cdots,\mathbf{r}_N)|^2,
$$
der vi for enkelhets skyld har sett bort fra at elektronet har spinn. Å ta med spinn gir bare en mer komplisert formel med mindre intuisjon, uten å endre resultatet. Dersom vi integrerer $\rho(\mathbf{r})$ over hele rommet, så ser vi at vi får
$$
	\int d\mathbf{r} \rho(\mathbf{r}) = N \int d\mathbf{r}_1 d\mathbf{r}_2 \cdots d\mathbf{r}_N |\Psi(\mathbf{r}_1,\mathbf{r}_2,\cdots,\mathbf{r}_N)|^2 = N\|\Psi\|^2 = N,
$$
som stemmer med at $\rho$ representerer en tetthet. *Elektrontettheten er hva vi mener når vi snakker om "elektronskyen".*

### Første Hohenberg-Kohn-teorem

Det første HK-teoremet sier kort sagt at dersom $\rho$ er tettheten som kommer fra en grunntilstand $\Psi$ for et molekyl med kjernepotensial $V_{\text{nuc}}$, da er $V_\text{nuc}$ bestemt opp til en konstant $\mu$, dvs., alle *andre* potensialer (ikke bare kjernepotensialer) som $\rho$ er grunntilstand for, er på formen $V = V_{\text{nuc}} - \mu$. Altså, dersom vi flytter på kjernene, selv bare ørlittegrann, så vil også tettheten endre seg.

Vi observerer at $V_\text{nuc}$ og $V_{\text{nuc}}-\mu$ har den samme grunntilstandsbølgefunksjon, og at det er bare ett valg av $\mu$ som gir et ekte kjernepotensial, nemlig $\mu=0$.

Vi kan nå gjøre følgende observasjon: Gitt en tetthetsfunksjon $\rho(\mathbf{r})$, så bestemmer denne funksjonen kjernepotensialet $V_\text{nuc}$ (opp til en konstant som vi kan sette til null). Men dersom vi kjenner kjernepotensialet, kan vi - i prinsippet - løse Schrödingerlikninga og finne grunntilstanden $\Psi$ til dette potensialet. Men da kan vi regne ut *alle forventningsverdier*, og dermed all fysikk! 

Med andre ord: Det er nok å vite tettheten for å bestemme løsningen av Schrödingerlikninga!

### Andre Hohenberg-Kohn-teorem

Det andre HK-teoremet sier at det finnes en funksjonal $F[\rho]$, kalt den universelle funksjonalen, slik at grunntilstandsenergien til $V_\text{nuc}$ kan skrives
$$
	E_0[V_\text{nuc}] = \min_{\rho}\left( F[\rho] + \int V_\text{nuc}(\mathbf{r})\rho(\mathbf{r}) \; d\mathbf{r} \right) \tag{$*$}
$$

En *funksjonal* er en funksjon av en funksjon. Tenk på en funksjonal som en funksjon som tar uendelig mange varable som innputt, og produserer ett eller flere tall som utputt. Vi har understreket i notasjonen på venstre side at grunntilstandsenergien er en funksjonal av potensialet.

Likningen $(*)$ kalles ofte "Hohenberg-Kohn-variasjonsprinsippet." Funksjonalen $F$ er "universell" i den forstand at den er gyldig for alle molekyler. Merk at vi har fiksert antall elektroner $N$ i denne sammenhengen, men prinsippet kan utvides til alle $N$.



## Levy-Lieb constrained-search-argumentet

Eksistensen av en universell funksjonal kan virke overraskende, men vi kan bruke et enklere argument som *ikke* tyr til HK-teoremene for å vise at den må finnes. 

Vi har dette uttrykket for forventningsverdien til Hamiltonoperatororen:
$$ 
\braket{\Psi|T_e + V_{ee} + V_\text{nuc}|\Psi} = \braket{\Psi|T_e + V_{ee}|\Psi} + \int \rho_\Psi V_\text{nuc} d\mathbf{r}.
$$
Her er $\rho_\Psi$ tettheten assosiert med $\Psi$, og vi understreker her avhengigheten med subskriptet.

Nå observerer vi at vi skal minimere denne forventningsverdien over alle normerte bølgefunksjoner. 
$$ 
E_0 = \min_{\Psi} \braket{\Psi|T_e + V_{ee} + V_\text{nuc}|\Psi} = \min_\Psi \braket{\Psi|T_e + V_{ee}|\Psi} + \int \rho_\Psi V_\text{nuc} d\mathbf{r}.
$$
Det er mange bølgefunksjoner som git opphav til samme tetthet. Men alle disse bølgefunkjonene gir samme forventningsverdi av $V_\text{nuc}$! Så vi deler opp minimeringen over $\Psi$ i (1) minimering over $\rho$ og (2) minimering over alle $\Psi$ som har tetthet $\rho$. Dette siste skrives $\Psi\mapsto\rho$. Da får vi:
$$ 
\begin{align}
E_0 &= \min_{\rho} \left(\min_{\Psi\mapsto\rho} \braket{\Psi|T_e + V_{ee}|\Psi} \right) + \int \rho V_\text{nuc} d\mathbf{r} \\
&= \min_{\rho}\left( F_\text{LL}[\rho] + \int \rho V_\text{nuc}\right).
\end{align}
$$
Den siste likninga definerer en Levy-Lieb-versjonen $F_{\text{LL}}[\rho]$ av den universelle funksjonalen. Den som nå er klart er at den representerer den kinetiske energien og elektronvekselvirkningene til faktisk alle bølgefunksjoner $\Psi$ slik at  $\Psi\mapsto\rho$.  

Sammenliknet med $F$ (fra HK2) er $F_{\text{LL}}$ eksplisitt definert. De to funksjonalene er matematisk *ikke* helt identiske, men gir opphav til samme grunntilstandsenergi.

De matematiske detaljene angår oss ikke. Vi vil heretter snakke om "den universelle funksjonalen $F$", og ikke bry oss om hvilket prinsipp den kommer fra. Den eksisterer!

Den universelle funksjonalen $F$ er en ekstremt komplisert funksjon som avhenger av $\rho(\mathbf{r})$ i alle punkter i rommet på en ekstremt innfløkt måte. Den er så innfløkt at vi ikke vet helt hvordan den ser ut. Det er rett og slett et mysterium! Matematikken gir oss i essensen stort sett bare at denne funksjonen *eksisterer*, og noen svært få hint om hvordan den eller ser ut. Men vi må gjøre kvalifiserte gjetninger og approksimasjoner for å komme noen vei videre.

### Oppsummering av fundamentet for DFT

Den veldig kompliserte $N$-elektron-bølgefunksjonen er byttet ut med en mye enklere tetthet, og at Hamiltonoperatorens komponenter $T_e + V_{ee}$ er byttet ut med den ukjente (og mye mer kompliserte) funksjonalen $F$. Grunntilstanden er gitt ved et variasjonsprinsipp.


## Kohn-Sham-teori

***Det er ikke meningen at du skal forstå denne "utledningen". Den er til orientering og målet er å gi en viss ide om hvor Kohn-Sham-likninga kommer fra, og hva de ulike symbolene betyr.***

Et vanskelig problem med DFT er at $F$ er så utrolig komplisert og vanskelig å modellere. Særlig to aspekter ved $F$ er vanskelige å kontrollere: Det er vanskelig å konstruere kinetisk energi fra bare tettheten alene, og det er vanskelig å modellere effekten av Pauli-prinsippet, "exchange", samt vekselvirkningene mellom elektronene, kalt "correlation" (korrelasjon på norsk, men vi bruker engelsk term her). 

I Hartree-Fock er begge aspekter lette å modellere - kinetisk energi er jo bare en operator, og pauliprinsippet gir "exchange-potensialet" $K$. Potensialet $J$ kalles "Hartree-potensialet" og er faktisk *ikke* vanskelig å modellere. Det er eksplisitt uttrykt ved tettheten $\rho$! Hartree-potensialet er det elektrostatiske potensialet generert av ladningstettheten $\rho$, og velkjent i elektrodynamikken:
$$
	J(\mathbf{r}) = \frac{1}{2} \frac{e^2}{4\pi\varepsilon_0} \int d\mathbf{r}' \frac{\rho(\mathbf{r'})}{|\mathbf{r}-\mathbf{r}'|}
$$
Den totale elektrostatiske energien er
$$
	E_{\text{Hartree}}[\rho] = \int d\mathbf{r} J(\mathbf{r})\rho(\mathbf{r}).
$$
Kohn og Sham hadde *den briljante ide* at man kunne gjenta HK-teoremene for et *ikkevekselvirkende system av elektroner*, og betrakte et slikt - fiktivt - system i et *annet* ytre potensial $V_\text{eff}(\mathbf{r})$. Dette potensialet tenkte de seg kunne velges slik at grunntilstanden for det fiktive systemet reproduserte den *eksakte* vekselvirkende tettheten. Hvorfor ikke-vekselvirkende? Jo, for da stryker vi bare $V_{ee}$ i Hamiltonoperatoren, som gjør Schrödingerlikninen lett å løse ved separasjon av variable, som gir
$$
	\Big[\frac{-\hbar^2}{2m_e}\nabla^2 + V_{\text{eff}} (\mathbf{r})\Big]\phi_i(\mathbf{r}) = \epsilon_i \phi_i(\mathbf{r}).
$$
Den eksakte ikke-vekselvirkende $N$-elektron-tilstanden er en Slater-determinant, akkurat som i Hartree-Fock-teori. 

Ved hjelp av HK-teoremene eksisterer det nå en universell funksjonal for ikkevekselvirkende systemer, kalt $F_\text{s}[\rho]$, slik at den ikke-vekselvirkende grunntilstandsenergien er
$$
	E_{0,\text{s}}[V_\text{eff}] = \min_\rho \left( F_\text{s}[\rho] + \int V_\text{eff}(\mathbf{r})\rho(\mathbf{r}) \right).
$$
Men samtidig vet vi fra separasjon av variable at $E_{0,\text{s}}[V_\text{eff}] = \sum_{i=1}^{N/2} 2\epsilon_i$. Vi vet også at tettheten til grunntilstanden er
$$
	\rho_\text{s}(\mathbf{r}) = 2\sum_{i=1}^{N/2} |\phi_i(\mathbf{r})|^2,
$$
som man kan vise direkte fra definisjonen.

Sett nå at $V_\text{eff}$ er justert *akkurat slik* at $\rho_s(\mathbf{r}) = \rho(\mathbf{r})$, den eksakte grunntilstandstettheten. Da har vi to betingelser oppfylt:
$$
	\begin{align}
	\frac{\delta}{\delta \rho}  F_\text{s}[\rho] + V_\text{eff}  &= 0, \\
		\frac{\delta}{\delta \rho} F[\rho] + V_\text{nuc} &= 0, \\
	\end{align}
$$
Ved sammenlikning får vi at
$$
	V_\text{eff} = V_\text{nuc} + \frac{\delta}{\delta\rho} (F[\rho] - F_\text{s}[\rho])
$$
Dette er en veldig banebrytende likning: Kohn og Sham viste at under antakelsen om at man kan derivere funsjonalene, så har vi en formel for det effektive potensialet! Dette understreker vi at gir en 1-elektron-Schrödingerlikning som er mye, mye lettere å løse enn det fulle $N$-elektron-problemet.

Det er vanlig å separere ut Hartree-energien, siden denne er kjent:
$$
	V_\text{eff}(\mathbf{r}) = V_{\text{nuc}}(\mathbf{r}) + 2J(\mathbf{r}) + V_{\text{xc}}(\mathbf{r}),
$$
der *exchange-correlation*-potensialet $V_{\text{xc}}(\mathbf{r})$ er relatert til en exchange-correlation *energi*,
$$
	E_\text{xc}[\rho] = F[\rho] - F_\text{s}[\rho] - E_\text{Hartree}[\rho]
$$
$$
	V_{\text{xc}}(r) = \frac{\delta E_{\text{xc}}[\rho]}{\delta\rho}.
$$
 Resultatet er en modifikasjon av Hartree-Fock-likninga som kalles ***Kohn-Sham-likninga,*** og ser ut som følger:
$$
	\Big[\frac{-\hbar^2}{2m_e}\nabla^2 + \underbrace{V_{\text{nuc}} (\mathbf{r}) + 2J(\mathbf{r}) +  V_{\text{xc}}}_{V_\text{eff}}\Big]\phi_i(\mathbf{r}) = \epsilon_i \phi_i(\mathbf{r}). \tag{$**$}
$$
Sammenliknet med Hartree--Fock-likninga ser vi at leddet $-K(\mathbf{r})$ er erstattet med $V_{\text{xc}}(\mathbf{r})$, som kalles "exchange-correlation-potensialet".  Det opprinnelige leddet $K$ var kalt "exchange" og kom fra pauliprinsippet. Nå har vi en mer avansert modell, der vi har både exchange *fra en mangepartikkelbølgefunksjon som ikke er en ren Slater determinant*, og correlation, som ikke er tilstede i en ren Slater-determinant. 


# Modell-funksjonaler

Ser vi på Kohn-Sham likninga, ser vi at det som er ukjent er $V_{\text{xc}}$. Ulike modeller for dette gir opphav til ulike "DFT-funksjonaler".

## Local density approximation (LDA)

I LDA antar man at XC-potensialet i hvert punkt i rommet kun avhenger av den lokale elektrontettheten $\rho(\mathbf{r})$, og det behandler systemet som om det var en uniform elektrongass. Det vil si at man antar at potensialet endrer seg så lite at man kan anta at elektrontettheten er så og si konstant. Dette er en tilnærming som er ganske shaky, men det gir OK resultat. Vi setter $V_\text{xc} = V_{\text{x}}^\text{LDA} + V_{\text{c}}^\text{LDA}$:

- **Exchange**: Exchangedelen i LDA bruker den eksakte løsningen for uniform elektrongass:
  
  $$
  V_{\text{x}}^{\text{LDA}}[\rho] = C \rho(\mathbf{r})^{1/3}
  $$
  Her er $C$ en konstant som bestemmes empirisk eller analytisk, avhengig av modellen.
  
- **Korrelasjon**: Korrelasjonsdelen i LDA er vanligvis tilpasset data fra kvante-Monte Carlo-simuleringer av uniform elektrongass. Da modelleres korrelasjonsenergien som
$$ 
E_{\text{c}}^{\text{LDA}}[\rho] = \int \rho(\mathbf{r}) \epsilon_{\text{c}}(\rho(\mathbf{r})) d\mathbf{r} .
$$
* Her er $\epsilon_c$ en empirisk funksjon. Den funksjonalderiverte gir
$$
V_{\text{c}}^{\text{LDA}}(\mathbf{r}) = \epsilon_{\text{c}}(\rho(\mathbf{r})) + \rho(\mathbf{r}) \frac{\partial \epsilon_{\text{c}}(\rho(\mathbf{r}))}{\partial \rho(\mathbf{r})}
$$

LDA fungerer overraskende bra for systemer med sakte-varierende elektrontetthet, som faste stoffer eller halvledere. Molekyler og atomer er dessverre ikke slik at tettheten er saktevarierende.

#### Eksempel på LDA-funksjonaler:
- **Vosko-Wilk-Nusair (VWN)** eller **Perdew-Zunger (PZ)** for korrelasjon. Dette er modeller for $\epsilon_\text{c}$.

## Generaliserte gradient-approksimasjoner (GGA)

**Generaliserte gradient-approksimasjoner (GGA)** forbedrer LDA ved å inkludere ikke bare den lokale elektrontettheten $\rho(\mathbf{r})$, men også gradienten $\nabla \rho(\mathbf{r})$. Dette gjør at funksjonalen kan ta hensyn til variasjoner i elektrontettheten på en mer effektiv måte. Intuitivt gir dette en beskrivelse av kinetisk energi.

- **Exhange**: LDA modifiseres til å inkludere en avhengighet av $\nabla \rho$:
  $$
   V_{\text{x}}^{\text{GGA}}[\rho] =  f\left( \rho(\mathbf{r}), \nabla \rho(\mathbf{r}) \right)
   $$
   Her er $f$ en funksjon med empiriske parametre.
  
- **Korrelasjon**: Korrelasjonsdelen korrigeres også med gradienttermer.
$$
E_{\text{c}}[\rho] = \int g(\rho, \nabla \rho) d\mathbf{r}
$$
	Her er $g$ en funksjon.
 
GGA-funksjonaler fungerer generelt bedre for molekylære systemer enn LDA, og gir mer nøyaktige bindingslengder, energier og reaksjonsbarrierer, for eksempel.

#### Eksempel på GGA-funksjonaler:
- **PBE (Perdew-Burke-Ernzerhof)**: En av de mest populære GGA-funksjonalene. God balanse mellom nøyaktighet og beregningskostnad.
- **BLYP (Becke-Lee-Yang-Parr)**: Kombinerer Beckes exchange med Lee-Yang-Parr korrelasjonsfunksjonalen. Gir generelt gode geometrier, reaksjonsenergier, og vibrasjonsfrekvenser for molekyler.

## Meta-Generaliserte Gradient-Approksimasjoner (meta-GGA)

**Meta-GGA**-funksjonaler bygger videre på GGA ved å inkludere ikke bare elektrontettheten og gradienten, men også **kinetisk energitetthet**. Da får vi enda mer fleksibilitet i modelleringen, men kostnadene går på den annen side opp. Den kinetiske energitettheten kommer fra Kohn-Sham-orbitalene og har uttrykket:
$$
\tau(\mathbf{r}) = \sum_{i=1}^{N} \phi_i^*(\mathbf{r}) \left( -\frac{\hbar^2}{2m_e} \nabla^2 \right) \phi_i(\mathbf{r}).
$$

- **Exchange**: Inkluderer en avhengighet av den kinetiske energitettheten:
  
$$
  V_{\text{x}}^{\text{meta-GGA}}[\rho] = f\left( \rho(\mathbf{r}), \nabla \rho(\mathbf{r}), \tau(\mathbf{r}) \right)
$$
  
  der $\tau(\mathbf{r})$ er den kinetiske energitettheten til Kohn-Sham-orbitalene.

- **Fordeler**: Meta-GGA-funksjonaler er enda mer nøyaktige enn GGA-funksjonaler.
  
- **Ulemper**: Mer beregningsmessig krevende enn GGA.

#### Eksempel på Meta-GGA-funksjonaler:
- **TPSS (Tao-Perdew-Staroverov-Scuseria)**: En av de mest brukte meta-GGA-funksjonalene.
- **SCAN (Strongly Constrained and Appropriately Normed)**.

## Hybridfunksjonaler

**Hybridfunksjonaler** kombinerer noe som kalles  **eksakt exchange** fra Hartree-Fock-teori med tilnærmet exchange og korrelasjon fra GGA- eller meta-GGA-funksjonaler. Den eksakte exchangetermen er rett og slett $-2K(\mathbf{r})$-leddet fra $V_\text{eff}$ i Hartree-Fock-teori, og er inkludert for å forbedre nøyaktigheten.

- **Exchange**: Man blander inn en fraksjon $\alpha$ av Hartree--Fock exchange med en fraksjon $(1-\alpha)$ av  (meta-)GGA exchange
  
  $$
  E_{\text{x}}^{\text{hybrid}} = \alpha E_{\text{x}}^{\text{HF}} + (1 - \alpha) E_{\text{x}}^{\text{GGA/meta-GGA}}
  $$
    der $\alpha$ er en blandingsparameter. Her gir den deriverte av $E_\text{x}^\text{HF}$ leddet $-2K(\mathbf{r})$ som finnes i Hartree--Fock-likningene.

- **Korrelasjon**: Som i GGA eller meta-GGA.

Hybridfunksjonaler er spesielt gode for organiske molekyler eller overgangsmetall-komplekser. Men, disse funksjonalene er enda mer kostbare å bruke, særlig eksakt exchange er dyrt (to-elektron-integraler.)

#### Eksempel på hybridfunksjonaler:
- **B3LYP (Becke, 3-parameter, Lee-Yang-Parr)**: En av de mest brukte hybridfunksjonalene.  Beckes exchange-funksjonal er kombinert med LYP-korrelasjon.
- **PBE0**: En hybridversjon av PBE-funksjonalen, med 25 % eksakt Hartree-Fock-exchange.


