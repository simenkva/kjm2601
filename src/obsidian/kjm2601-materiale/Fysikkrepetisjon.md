#notat #kjm2601 

# Molekylet som klassisk mekanisk system

## Partiklene i et molekyl

I dette kurset skal vi tenke som fysikere, og betrakte atomer og molekyler som systemer av partikler som følger kvantemekanikkens lover. Men kvantemekanikk bygger på klassisk mekanikk, og dessuten er det slik at atomkjernene som regel kan behandles som klassiske partikler. Derfor tar vi en liten sesjon hvor vi diskuterer atomer og molekyler som klassiske partikler - selv om vi det at dette er "feil".

Et molekyl består av flere partikler:
- elektroner (elementærpartikler)
- protoner (kompositte partikler)
- nøytroner (kompositte partikler)

Protonene og nøytronene -- nukleoner -- er så sterkt klumpet sammen av _den sterke kjernekraften_ at de utgjør en enhet som er veldig vanskelig å dele opp - atomkjernen. Atomkjernen består av $Z$ protoner og $N$ nøytroner, og det er totalt $A = N + Z$ partikler i kjernen. Massen er summen av massene til protonene og nøytronene, Atomkjernen har en utstrekning $R$ på størrelsesorden av femtometer (aka fermi), og er veldig hard. 
 $$ R \approx R_0 \cdot A^{1/3}, \quad R_0 \approx 1.2-1.3 \; \text{fm} $$
En fermi er $10^{-15}$ m. Til sammenlikning er hydrogenatomets utstrekning $5 \cdot 10^{-11}$ m. Det er en faktor 10000. Så mesteparten av et atom er faktisk tomrom.
  
Nøytronene er elektrisk nøytrale, mens protonene er ladet, med ladning $e$, der $e$ er elementærladningen. (Faktisk er det slik at protonene består av to oppkvarker og en nedkvark, og nøytronene består av en oppkvark og to nedkvarker. Nedkvarker har ladning $-1/3e$ og oppkvarkene $+2/3e$. )

Selv om kjernene er så ekstremt små, er nesten all atommassen konsentrert der. Det er vanlig å ignorere utstrekningen til kjernene, og anta at de er punktpartikler.

Elektronene på sin side er elementærpartikler, og så langt vi vet er de punktpartikler. De har ingen målbar utstrekning! Elektronene har ladning $-e$.

## Posisjon, hastighet, og akselerasjon, og Newtons 2. lov

![[elektronposisjoner_og_atomkjerner.svg]]

Når vi behandler subatomære partikler klassisk har de en _veldefinert posisjon og hastighet til et hvert tidspunkt._ Partiklene _vekselvirker_, det vil si at de påvirker hverandre med krefter, ved Coulombs lov. Til hvert elektron $i$ (der $i=1,2,\cdots,N_e$ med totalt $N_e$ antall elektroner) har vi da en vei $\mathbf{r}_i(t)$ som funksjon av tiden $t$. Til hver atomkjerne $a$ (med $a=1,2,\cdots N_{at}$ med $N_{at}$ totalt antall atomer) har vi en vei $\mathbf{R}_a(t)$. Hastigheten til elektronene og kjernene er gitt ved derivasjon med hensyn på tid,
$$ \mathbf{v}_i(t) = \frac{d}{dt} \mathbf{r}_i(t). $$
$$ \mathbf{V}_a(t) = \frac{d}{dt} \mathbf{R}_a(t). $$
Akselerasjonen er den annenderiverte:
$$ \mathbf{a}_i(t) = \frac{d}{dt} \mathbf{v}_i(t) = \frac{d^2}{dt^2} \mathbf{r}_i(t). $$
$$ \mathbf{A}_a(t) = \frac{d}{dt} \mathbf{V}_a(t) = \frac{d^2}{dt^2} \mathbf{R}_a(t). $$
Vi skriver $m_e$ for elektronmassen, og $M_a$ for massen til atomkjerne nummer $a$. Elektronene har ladning $-e$ og hver kjerne $Z_ae$,, der $Z_a$ er antall protoner i kjernen.

Disse veiene bestemmes av Newtons andre lov:

> [!NOTE] Newtons annen lov
> Akselerasjonen $\mathbf{a}$ til en partikkel med masse $m$  er gitt ved
> $$ m \mathbf{a} = \mathbf{F}, $$
> der $\mathbf{F}$ er summen av alle de ytre kreftene som virker på partikkelen.

## Coulomb-krefter

For å gjøre livet litt enklere en stund, så velger vi en matematisk notasjon som ikke skiller mellom elektroner og atomkjerner. De er tross alt "like" i den forstand at de er partikler med masse og ladning og neglisjerbar utstrekning. Så nå bruker vi $i$ som indeks for alle partiklene, slik at $i=1,2,\cdots,N$, og , $m_i$ for massen til partikkel nummer $i$, $q_i$ for ladningen, $\mathbf{r}_i(t)$ for posisjon, og prikknotasjon for hastighet og akselerasjon:
$$ \mathbf{v}_i(t) = \dot{\mathbf{r}}_i(t) = \frac{d}{dt} \mathbf{r}_i(t). $$
$$ \mathbf{a}_i(t) = \dot{\mathbf{v}}_i(t) = \ddot{\mathbf{r}}_i(t) = \frac{d^2}{dt^2} \mathbf{r}_i(t). $$
Hva er de ytre kreftene på et partikkel $i$? To ladede partikler med ladning $q_1$ og $q_2$ separert med en avstand $r$ vekselvirker med Coulombs lov.  Den beskriver kreftene ved hjelp av et _potensial_ gitt som
$$ V_{\text{C}}(r) = \frac{1}{2\pi \epsilon_0} \frac{q_1 q_2}{r} $$
Potensialet har dimensjon energi. Dersom partikkel 1 er i $\mathbf{r}_1$ og partikkel 2 i $\mathbf{r}_2$, så har vi
$$ r = r_{12} = |\mathbf{r}_1 - \mathbf{r}_2| = \sqrt{(x_1-x_2)^2 + (y_1-y_2)^2 + (z_1-z_2)^2}.$$
Coulombs lov sier nå at kraften som partikkel $1$ føler fra 2 er
$$ \mathbf{F}_{12} = -\nabla_{1} V_{\text{C}}(r_{12}). $$
Her er $\nabla_i$ gradientoperatoren for koordinatene til partikkel $i$. Det er en øvelse å regne ut denne kraften. (Det kan være lurt å bruke kjerneregen, og først regne ut $\nabla V_\text{C}$. ) Svaret er
$$ \mathbf{F}_{12} = - \frac{q_1q_2}{4\pi\epsilon_0} \frac{\mathbf{r}_2-\mathbf{r}_1}{r_{12}^3} , \quad \mathbf{F}_{21} = - \mathbf{F}_{12}. $$

Merk at $\mathbf{r}_2-\mathbf{r}_1$ er forskyvningsvektoren mellom 1 og 2, og lengden $r_{12}=|\mathbf{r}_2-\mathbf{r}_1|$ er avstanden. Så kraftens størrelse er
$$ |\mathbf{F}_{12}| = \frac{|q_1||q_2|}{4\pi\epsilon_0} \frac{1}{r_{12}^2}. $$
Kreftene på 1 og 2 er like store, og motsatt rettet. Dette er et eksempel på Newtons 3 lov:


> [!NOTE] Newtons 3. lov
> Til enhver kraft fra ett legeme på annet tilsvarer en like stor og motsatt rettet kraft fra det andre legemet på det første.

## Newtons 2. lov for Coulombkrefter

Nå har vi ingrediensene vi trenger for å skrive ned bevegelseslikningene til et system av ladede partikler. Betrakt partikkel nummer $i$. Alle de andre partiklene, $j\neq i$, påvirker partikkelen med Coulombkrefter:
$$ m_i \ddot{\mathbf{r}}_i(t) = - \sum_{j\neq i}  \frac{q_i q_j}{4\pi\epsilon_0} \frac{\mathbf{r}_j-\mathbf{r}_i}{r_{ij}^3} . $$
Dette er et system av  _annenordens ordinære differensiallikninger_.

Så, tenker vi oss at vi starter i $t=0$, kan vi nå bestemme _historien_ til systemet av partikler dersom vi kjenner alle _initialbetingelsene_ $\mathbf{r}_i(0)$ og $\dot{\mathbf{r}}_i(0)$. Merk at akselerasjonen ikke avhenger av hastighetene, kun posisjonene. Men hastigheten i $t=0$ er ikke bestemt av likningen. Derfor må vi supplere disse betingelsene.

## Hamiltons bevegelseslikninger

Nå skal vi beskrive det som kalles _Hamiltons bevegelseslikninger_. Dette er en elegant omskriving av Newtons 2. lov for konservative systemer, det vil si systemer der kreftene er gitt som gradienter av potensiell energi.

Vi legger merke til at dersom vi definerer _total potensiell energi_ gitt som
$$ V(\mathbf{r}_1,\cdots,\mathbf{r}_N) = \sum_{(i,j)}^N V_\text{C}(\mathbf{r}_i-\mathbf{r}_j), $$
der summasjonen går over alle distinkte _par_ $(i,j)$ av partikler, så kan den totale kraften på partikkel $i$ fra alle de andre partiklene skrives som
$$ \mathbf{F}_i = -\nabla_{\mathbf{r}_i} V(\mathbf{r}_1,\cdots,\mathbf{r}_N). $$
Vi innfører nå _bevegelsesmengden_ $\mathbf{p}_i = m_i \mathbf{v}_i = m_i \dot{\mathbf{r}}_i$ til partikkel nummer $i$. Vi merker oss at
$$ \dot{\mathbf{r}}_i = \frac{1}{m_i} \mathbf{p}_i = \nabla_{\mathbf{p}_i} \frac{|\mathbf{p}_i|^2}{2m_i}. $$
Her er $|\mathbf{p}_i|^2/(2m_i) = m_i \mathbf{v}_i^2/2$ den _kinetiske energien_ til partikkel nummer i. Vi definerer, i likhet med potensiell energi, _total kinetisk energi_,
$$ T(\mathbf{p}_1,\cdots,\mathbf{p}_N) = \sum_i \frac{|\mathbf{p}_i|^2}{2m_i}. $$
Vi har nå et system av _førsteordens differensiallikninger_
$$ \dot{\mathbf{r}}_i = \nabla_{\mathbf{p}_i} T(\mathbf{p}_1,\cdots,\mathbf{p}_N), \quad \dot{\mathbf{p}}_i = - \nabla_{\mathbf{r}_i} V(\mathbf{r}_1,\cdots,\mathbf{r}_N). $$
Dette begynner å se interessant ut! Vi definerer nå _total energi_, eller _Hamiltonfunksjonen_, som
$$ H(\mathbf{r}_1,\cdots,\mathbf{p}_N) = T(\mathbf{p}_1,\cdots,\mathbf{p}_N) + V(\mathbf{r}_1,\cdots,\mathbf{r}_N). $$
Siden $T$ ikke avhenger av posisjon, og $V$ ikke avhenger av hastigheter (bevegelsesmengder), og dersom vi introduserer notasjonen $\mathbf{r} = (\mathbf{r}_1,\cdots,\mathbf{r}_N) \in \mathbb{R}^{3N}$ og $\mathbf{p} = (\mathbf{p}_1,\cdots,\mathbf{p}_N)\in \mathbb{R}^{3N}$, kan vi kondensere Newtons annen lov til en veldig elegant likning som kalles _Hamiltons bevegelseslikninger_:


> [!NOTE] Hamiltons bevegelseslikninger
> $$ \dot{\mathbf{r}} = \nabla_{\mathbf{p}} H(\mathbf{r},\mathbf{p}), \quad \dot{\mathbf{p}} = - \nabla_{\mathbf{r}} H(\mathbf{r},\mathbf{p}). $$
 
Vi ser nå at $\mathbf{r}(0)$ og $\mathbf{p}(0)$ er intialbetingelsene til hele systemet av $N$ ladede partikler, og dersom vi kjenner disse, vil Hamiltons bevegelseslikning for all fremtid bestemme posisjonen og hastigheten til alle partiklene.

Merknad: Vi kan abstrahere enda litt mer, og definere et _faserom_ $\mathbb{R}^{2(3N)}$ med punkter $\xi = (\mathbf{r},\mathbf{p})$. Merk at et punkt $\xi$ i faserommet bestemmer tilstanden til partikkelsystemet unikt.

Vi definerer den _symplektiske matrisen_ $J$,
$$ J = \begin{pmatrix} 0_{2N} & -I_{3N} \\ I_{2N} & 0_{3N} \end{pmatrix}. $$
Da kan vi skrive Hamiltons likninger som:
$$ J \dot{\xi} = \nabla_\xi H(\xi). $$
Vi skal ikke bruke denne abstrakte formuleringen videre.

## Energibevaring

Bevaring av energi: Hamiltons bevegelseslikninger er nyttige. For eksempel er det ganske greit å regne ut at _total energi er bevart_. Den totale energien skriver vi som 
$$ E(t) = H(\mathbf{r}(t),\mathbf{p}(t)), $$
altså summen av kinetisk og potensiell energi for _alle_ partiklene i systemet, langs veien de faktisk tar i rommet. Deriverer vi med hensyn på $t$ og bruker kjerneregelen får vi med en gang at
$$ \frac{d}{dt} E(t) = 0. $$
Se hvor lett Hamilton formalisme gir oss bevaring av energi for et konservativt system!


Den hamiltonske formalismen er viktig, for det er denne som er utgangspunktet for kvantemekanikken.

## Hydrogenatomet

Det kan være instruktivt å se på den klassiske bevegelsen av 1-elektronsystemer. Vi velger å sette massene til atomkjernen til uendelig, slik at det bare er elektronet som beveger seg. Vi vil se på hydrogenatomet og $H_2^+$ kationet. 

For H-atomet setter vi protonet i origo, og grunnet symmetri vil elektronet bevege seg i et plan, som vi velger til å være $xy$-planet, med altså $z=0$. (Vi kunne også brukt analytiske metoder og beskrevet 2-partikkelsystemet i massesenter og relativkoordinater. Resultatet blir i essensen det samme.)

Elektronets potensielle energi er
$$ V(x,y) = -\frac{e^2}{4\pi\epsilon_0} \frac{1}{\sqrt{x^2+y^2}}. $$
Vi setter lengdeskalaen slik at $e^2/4\pi\epsilon_0=1$ (atomære enheter).

Bevegelsen til elektronet i H-atomet har velkjente løsninger, og sammenfaller med bevegelsen av en planet rundt en sol, siden gravitasjonskrefter har samme form som Coulombkrefter. Slik "Kepler-bevegelse" er periodiske ellipsebaner, med solen i ett av fokalpunktene dersom total energi er mindre enn null, parabelbaner dersom energien er null, og hyperbolske baner dersom energien er større enn null.

Vi kan forsøke å løse problemet numerisk. Jeg har laget en Jupyter notebook (`classical_molecule_dynamics.ipynb`), der vi løser bevegelseslikningene til $N$ ladede partikler med numeriske metoder - her den såkalte _leapfrog-metoden_. I notebooken kan vi sette opp partiklenes masse, ladning og startposisjoner og -hastigheter, for så å simulere. Deretter lages det en animasjon.

For H-atomet må vi ha en kjerne og et elektron. Simuleringene blir gjort i atomære enheter, der $m_e = 1$ og $m_p = 1836$. Videre er $e = 1$. Vi legger protonet i origo og elektronet i punktet $(x,y) = (1,0)$, med hastighet $(v_x,v_y)=(0,1)$. Dette er valgt slik at vi da skal få sirkelbevegelse for elektronet (til en veldig god tilnærming).


```python
N = 2 # Number of particles
dim = 2 # Dimension of the system
mass = np.array([1836, 1]) # Mass of the particles
charge = np.array([1, -1]) # Charge of the particles
pos = np.array([[0, 0], [1.0, 0.0]]) # Initial position of the particles
vel = np.array([[0, 0], [0, 1.0]]) # Initial velocity of the particles
dt = 0.01 # Time step
t_final = 10 # Final time

pos_t, vel_t = integrate_leapfrog(pos, vel, mass, charge, dt, t_final)
```

Her er animasjonen som blir produsert:
![[h_classical_orbit.mp4]]

Vi ser at vi får en periodisk og fine bane, og at det svært tunge protonet ligger mer eller mindre i ro under hele dynamikken.

Vi kan endre litt på initialhastigheten til elektronet. Da er ikke lenger banen sirkulær, men elliptisk, med protonet i ett av fokusene.

```python
N = 2 # Number of particles
dim = 2 # Dimension of the system
mass = np.array([1836, 1]) # Mass of the particles
charge = np.array([1, -1]) # Charge of the particles
pos = np.array([[0, 0], [1.0, 0.0]]) # Initial position of the particles
vel = np.array([[0, 0], [-0.4, 1.0]]) # Initial velocity of the particles
dt = 0.03 # Time step
t_final = 30 # Final time
```

![[h_classical_orbit_elliptic.mp4]]

## Hydrogen-kation

For $H_2^+$ har vi to protoner. Vi legger disse i to punkter med en avstand $R$. Av symmetrigrunner kan vi velge romkoordinatene $(R/2,0,0)$ og $(-R/2,0,0)$. Nå har ikke systemet lenger en symmetri som gjør at elektronet vil forbli i et plan, med mindre $z(0)=0$. Vi skal forsøke å gjøre en numerisk løsning og plotte resultatene.

```python
N = 3
dim = 2
mass = np.array([1836, 1836, 1])
charge = np.array([1, 1, -1])
pos = np.array([[.1, 0], [-.1, 0], [1.0, 0.0]])
vel = np.array([[0, 0], [0,0], [0.0, 1.0]])
dt = 0.01
t_final = 10
```

Her er resultatet:

![[h2plus_classical_orbit.mp4]]


Vi ser en ganske forvirrende bane, og etter et par-tre runder så stikker elektronet rett og slett av etter å ha kommet for nærme et proton. Dette er et vekjent fenomen innen _trelegemeproblemet_: Systemet er ustabilt og på ett eller annet tidspunkt vil partikler bli sendt ut mot uendelig.

Hva er det forresten som skjer med protonene her? Merk at de er initiellt plassert veldig nær hverandre.

Husk at dette er _klassiske simuleringer_. Molekyler er kvantemekaniske, og det er et ganske dypt faktum at mangelegemeproblemet er stabilt når det er kvantemekanisk. Årsaken til dette kan sies å være Heisenbergs uskarphetsrelasjon, men dette kommer vi tilbake til senere.


## Generelle konservative systemer

Vi startet med et system av ladde partikler og endte opp med en Hamiltonfunksjon og Hamiltons likninger for bevegelse. På en måte kan vi jo si at Coulomb-kreftene er alt vi trenger, dersom vi antar at vi ønsker å skrive ned bevegelseslikningene til et fysisk system. Alt er atomkjerner og elektroner! Eller er det det ... ?

For det første er det enormt komplisert å skrive ned bevegelseslikningene til, for eksempel, en kaffekopp dersom vi insisterer på at alle atomene skal være med. På den annen side finnes det mer enn atomer i den klassiske verden vi må beskrive - vi har også _elektromagnetiske krefter_.

### Harmonisk oscillator

Vi starter med det første temaet. Hamiltons likninger kan brukes også til å modellere generelle klassiske systemer, slik som en kopp, en pendel, you name it. Så lenge vi kan skrive ned en Hamiltonfunksjon kan vi utlede bevegelseslikninger og i prinsippet løse disse. Vi skal ta for oss ett eksempel som hjelper oss med intuisjonen: en 1-dimensjonal harmonisk oscillator, som modellerer en mekanisk fjær.

Se for deg en fjær fastspent i taket, med et lodd med masse $m$ i enden. Gravitasjonen trekker på loddet, og fjæra trekker i motsatt retning, slik at vi får en likevekt. Kraften på loddet er da null. Posisjonen til loddet setter vi til å være $y=0$. Dersom vi strekker fjæra og slipper, vet vi av erfaring at loddet vil utføre jevn svingebevegelse.
![[spring.svg]]
Kreftene som fjæra yter på loddet kan til en god approksimasjon skrives som
$$ F(y) = -ky, $$
der $k$ er en konstant som kalles _fjærkonstanten_ og $y$ er utslaget i vertikal retning relativt til likevekten. Jo lenger vekk fra likevekt, jo sterkere trekker fjæra. Merk at kreftene er alltid rettet mot likevekt $y=0$. Det er ikke så vanskelig å se at
$$ F(y) = - \frac{d}{dy} V(y), \quad V(y) = \frac{1}{2} k y^2. $$
Altså er svingebevegelsen laget av en konservativ kraft, siden den er en gradient. (Vi ser bare på $y$-bevegelse, så da er kreftene alltid konservative, siden vi alltid kan finne en antiderivert til $F(y)$!) 

Videre vet vi at loddet i bevegelse har kinetisk energi $T = \tfrac{1}{2}m v_y^2 = \tfrac{1}{2} p_y^2/m$ der $p_y = mv_y$ er bevegelsesmengden i $y$-retningen. Dette gjelder for alle masser i bevegelse. Da får vi Hamiltonfunksjonen
$$ H(y,p_y) = \frac{1}{2m} p_y^2 + \frac{1}{2}k y^2. $$
Vi ser altså bort fra mulig bevegelse i de andre romlige retningene.

Hamiltons likninger lyder nå:
$$ \dot{y} = \frac{1}{m} p_y, \quad \dot{p}_y = - ky. $$
Kombinerer vi de to, får vi Newtons annen lov:
$$ \ddot{y} = -\frac{k}{m} y. $$
Dette kunne vi lett sett fra det faktum at de totale kreftene er $-ky$, siden $m\ddot{y} = F$ fra Newtons annen lov. Men Hamilton gir oss mer. For eksempel vet vi at den totale energien er bevart, og det er også generelt lettere å løse et førsteordens difflikningssystem enn et annenordens system.

Den generelle løsningen til bevegelseslikningen er standard innen difflikningsteori, og er
$$ y(t) = A \cos(\omega t) + B\sin(\omega t), \quad \omega = \sqrt{\frac{k}{m}}. $$
Her er $A$ og $B$ konstanter som bestemmes av initialbetingelsene. Vi velger disse ved å slippe $m$ fra ro ved $y = y_0$, dvs. $y(0) = y_0$ og $p_y(0) = 0$. Ved innsetting får vi da $y_0 = A$ og $B = 0$. Altså,
$$ y(t) = y_0 \cos(\sqrt{k/m}t). $$
![[potential_energy.svg]]

Det er nyttig å visualisere $y(t)$ sammen med $V(y)$, og gjøre noen betraktninger rundt energi. Vi vet at total energi er bevart, og total energi er bestemt av intialbetingelsene. Både $T$ og $V$ er positive størrelser, og bevegelsen vil endre $T$ og $V$ slik at summen er konstant. Den minste verdien for $T$ er null, og da får vi at $V = ky(t)^2/2 \leq E$. Da får vi
$$ |y(t)| \leq \sqrt{2E/k}.$$
Dette er illustrert i figuren. Området utenfor de vertikale linjene kalles "det klassisk forbudte området". For den gitte energien er det helt umulig at $y(t)$ kommer innenfor dette området.

Vi kan også si at den minste potensielle energien er $V=0$, som skjer når $y(t)=0$. Da er all energi bevegelsesenergi, og hastigheten er på sitt største der.

Her er en animasjon som viser bevegelsen. De vertikale linjene viser de klassisk forbudte områdene, og den horisontale linjen viser total energi. Animasjonen er laget med notebooken `classical_dynamics_1d.ipynb`.

![[classical_harmonic_oscillator.mp4]]


## Berg-og-dalbane-analogi

Dersom vi, slik som over, animerer fjærbevegelsen i potensial-plottet legger vi merke til at det på en måte ser ut som om massen "sklir" på en berg og dalbane med høyde $V(y)$. Dette er en nyttig analogi, og er *nesten* riktig. Om en masse $m$ skled friksjonsløst på en faktisk bane med form $V(y)$, for vilkårlige funksjoner, så er bevegelseslikningene nesten på Hamiltonsk form. Men for en "ekte" berg og dalbane er kreftene ikke eksakt gitt ved $-dV(y)/dy$. Det er likevel et nyttig bilde å ha. I figuren vises en potensialkurve og et markert punkt, samt en pil som indikerer kraften i punktet. Her er $V(y)$ gitt som:
$$ V(y) = -\frac{1}{y^2 + .24} - \frac{2}{(y-2)^2 + .3)} $$



![[double_well.svg]]

Her er bevegelsen for dette systemet animert:

![[classical_double_well.mp4]]

## Flere dimensjoner


Går vi til en 2-dimensjonal bevegelse, er $V(x,y)$ potensialflaten. Kraften er $F(x,y) = -\nabla V(x,y) = (-\partial F/\partial x, -\partial F/\partial y)$. Plotter vi $V$ med ekviverdikurver, så er kreftene alltid _ortogonale på konturene_. Dette gjør at vi kan danne oss en forventning om hvordan en partikkel vil bevege seg. I figuren er noen vilkårlige punkter valgt og (de  negative) gradientene er vist med røde piler.


![[potential_energy_2d.svg]]


Bevegelsen for partikler i 3d har _mange_ dimensjoner: Bare for He-atomet er det 6 dimensjoner for elektroner og 3 for kjernen, altså en 9-dimensjonal vektor for posisjon og tilsvarende for momentum. Altså er $\mathbf{r}(t) \in \mathbb{R}^9$ og $\mathbf{p}(t) \in \mathbb{R}^9$. Dette er ikke så lett å visualisere.

Dette avslutter vår repetisjon om klassisk mekanikk. Riktignok er det litt abstrakt, men det er nyttig når vi senere skal videre til kvantemekanikken.


