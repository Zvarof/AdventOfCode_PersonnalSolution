import re
from dijkstar import Graph, find_path

Input="""221132133212311232212242114141432412314342344414511125222353555313224255144252512523312445214535353432244331111334213433323123231313121233312
112212122221212221323211422324232212343312251322531451424155421523333223554153341151413325324333253423134212341243431224144312132322221323221
213313213322123132231341233221443443232132311221233553234412331241455332545534513324434532554435513521433123414411413332112232121311231333313
122111322123111123342223221344432441335345141551542425425323413343112243315451213441254551322425234511553143114414112321444431323332221131311
321211111212212332431213423112424233322543152513453155251312552321345542153421344235521424434323522543254212232311242124343311213232313122321
322123133221121212344241441112431241254234511433135241544144142451251221455341154114125414423454441551133123443333241142124141122321122112111
123311112232214444142223314414421343411243122531123115311142221552433342324343524443355534321225125453122445223233441132323142134213112323321
333221311221222332233211423323431443452223414535345514513523452455363552452646464223322124133135454453142341114322144233234433341122332223223
122212132211311131211311441422143155122512433323345543466366455336563642233222334226546222422553531344421412353311241312334224111322333123323
321233231131111321411243114422141523552423515544341563266535264525334422235652233425226566424521131545111553254142242134314342343144322123211
323212213142142423112441133423512142525542134141425223236344455535646256546256242425523555456555532422251511342425533441143123221431323133332
212112312442111222241343142523144552432312122135246436664646553456454433552225254343326555543553543213134542525532223143412132212444421213223
321211211241124211412342411411233152253114443525544225524634455536664462454325465464454433435624665424451311515523242134123224432222243313311
131333122213242331134143535143554345454411343565626562452463456645344623266565625336656545522642655244235144314124213234431114441132124132322
131312123321133113442331124114512351232556662642445566554562335632566323564355652332462546232642436346552153551321125542331144322412231141112
212333221311221443134123554454531543126654422265242653422665532252626634646643664534433326562653363433564445333443232345254341314122432241213
223132432344411434251542222114532535542555566626634526343255622622524353365566432563536656225524322332546442122452215352525133423212333232123
223441413243113433554115323311433352324324556246232542242522256443755653567344442353622255363623645334355543232424453452215313223224231122243
333444232422123141212323551311344253363463433432245264422622773367675554757474475755366235532333225325324533235434211244523125231142141422332
211432132423314455152434342234532542454644424624634665653476335636546347563676544577337343542236432225226535626234225112411124214111312122241
114213313132411513221552241515354334266554255426343235453363357477637353643436754665535577223346322525534356553533232511343125444421414233431
112414224141222225354131521253432354642344334636467667457755544357436544453633776435756465344434444426422263523335334535352244234431111121131
242224121434441313555321445133266233526222336565754535744754647363336365445345663364644665467364436242324545525265235322343423335533323321411
134323142234224355443552555263552564332333252244477676335465655336563674466535374436474463333364322556422353662536224324151522125312421141221
231443224113522352134253526625546664346232256636553464357563557343475534476347456356737556757455474632452533552566326121242145345544124242113
242121244233435241152524254436645532225633266743633374565557577455643443377764337647733354743554555544324532424544623344245254534215123214441
334224211324514255334534544656335353362345476556764633665557676557443775655477646347673357376663446673464243635222466444145325422431544341234
324434342342343123444546432562436635634337675453454746544577546644735463654477547375566766545567453665566222323462244334513252425344513134443
311414334114311313455155424564643323445645743575774674435433335766886745454865466737667667476366743555543665445656635424422523312515322114131
422412335432454455315526656222225266274546547734445547367656866757587576766766658785677557555465445767553325552464223362612435444315542142144
333442123352112433522423464526653652547743343347547457374775865774574856757644757888846546457743337366347673424434266534464331542524525523432
444322153141141242336623623236446463335767536773337763444647574574875778855546584787856667433666534335666377346343235355454214252434231312441
141334341542541143443565262434345544763674335563755668877846755785688845657777454488847854857364473466357747662454462352456513334312153412244
123124553134311442126262556523245745445437435337666458478754664544457564864485665757758644788456653777445666675365635562465555451535333144321
233224433352345124626553254344243337563434764345584584566667785658644574785766766455845877488677654446436753663445355524653345242144224421331
211325121323214542223235634662646657633356633356866565774557474646784564468476788666745548557866566665354776673535333225424233313234452222112
241321251234144134563466566425376643634554664787455546684448785877547668857746845748577477675884773555757373543554223355633332255252245213234
321513253111551465665332442323475577633745665886467445457847745646755647468775584867647588567555886677563667664533336644545425544415545445431
341553125534544436563226436274657334674644587567565866874646577448785586546675778644756646848658775437755546546755342253342663341544421121413
431125343151331344325423553336346473764435757585487886846777755685778957556566565885454465584775656857677355543563434565555364341142254511224
325544334354542235665246344355344765376365866654668554586755598558758597597799999654856884575467878567767573366373654334334565652212522352452
322553445332446556454336453755333566356744667568868854477846877777598999577765995779674788564546756656556354777766533242443332666314254431413
213332441515534535325645623777735366374767558876765668464857757995688675666596959866675544584477585577664466437467653663254664665554312553452
452455341321156655446455443333663576648884877754768777467556597896679555886869566668875945478867764845656364344364444353236235253234222545355
544124352122322564642223447454466754477556856856677457987875765596758659897997685579856678468474587554467564776656663663465463336263325114555
444435511353262255444422345465456476684768754774675666757955986567899786777688778679758595685664566666486837735533746373632632266355324541234
111115545433656543553663457455544355577484687474886775765956765588878757669676576566568878577488656448586644447763765755442446355243454232411
242425155325562635365337563465757567887854757784569977599677689765898679659589979698589758586677556557678586763535745547246225663436125342343
251333143215336246346244656567753377488885446587797778957677877895697769757598785887695668775858777885645784546435755534432234262463541112142
452441311522626255666535644557733355685575767868776795859755768886787795575986965876556999966986744447775466756363646453522266355426531325422
411414331353436555345763374665563675868676465589959669685769675958678798896668999985859989865975885477868854684377365545332336346553253435234
345545223452366642552346533764555578758454648778965769679978585666776887687969667995755698669568686467748677875774753467454523566243641111245
311133345456535342232357574576334647778765765856965888988789869799696678767798898779596968878955968666744778468643736356653223565442241111344
213312545464436556644544676374554758576458548699558588678699876787979888777979666698758759969656957755678847485556435534664266624333625214511
452341221343445546626567355365474567868655858689865969997597867886667898878979696686958556888566989656755585768476657474435353363526563322145
313521153532664625323577475777644756756885877759757658785978787796697987966778779798988665657588869556875565558475333356763535362335633334525
434532544242425342547566756446758584547555868759867676896968669676898889879768986698696865975999875645466478774443766663336325262543423225533
515445212524253355267466544657575586568854988995577565676998798688996896987798988698866765859878678975445766657576735777457362463535356544113
223244245643324566533764763653777767456846675598955896799997777899777899777699988999796888566997979686476474656864443354455654664236326544123
453244145262536455556645445435788758676447888578889996888686998986886896778688768696879778868559686865446778478873543354377726565345642635413
241443166422353334467646457354556886575547699888586788667797698768889886869899787696879967957788995885844588747787644576434645562423222523541
315514425545525643446455775675657578578697589986999897777987677976787999978779968688886769778659696688768744658446465446466554656236462635345
254524262543664365735363555544788464778555969996876896776679887888897898877778899897876679797855986978547545748465654737356366663225655334242
223411566666255524735656554438447648447658796968659688896876698889997999999778877667987699788856995865944875548684677647476534225445323343244
344424325243356323464366773638775645778796867669877687879766779798899897988798786688798987998788987677988884786586443663337736464624244655241
541221453563264662764736464554566856644999556759976979979786869998987779898778787798799876769686775758897587588666864367764753624534525311115
111422523442464633645344556376474657445588765556987969988876788898888987987797777687668697966786898855976488767767633363363665544556462543425
331521425234325366775664774388848675447675895568878669889699697987799887998779888768677778978777657557574555474588753574356564242255255252131
421345443235254654463735647355887668766966699667679776676768779989898997977989878779886887778696579578766765667554566564567465352626664252314
434412236664255645735677334385654748544959767997866677669696887887799777987777777989976799868998685865784657747685575443345466333644434545144
223311566244625335344765446374455555667965575558599786997897878887778879797988878779679696898755977786987578745567576475353446266246323431325
314554663254444225564355774355648844784657755567598979987668798789797878799999877977697789678879756765784754855545764553747337365655432333213
214241462244536666534454733558548666665585697959578889776896797888989977898878799787698779767798966688876784884756756753636774263552635525421
553233335323242443677657457487857488487697588878688878697688997999779978797799798889988668787557786955577865567745547576647634552223542663412
544351422322646555465665643444554587548899666759576997889878697787789777788797989997679667996568589699568568764564634653555436623343325441431
523533524462455443343446653544488755567798888689859768877899998879897999977978977968888796867965898776564847645468534567433774624335236345242
124441166644356567665754675364788654888576575667769978689687979798799797887889797789696688988976795697684845885856573775354464432342236314352
234421163646444322643536334464887868687797555557798676978997899998979888779979798876897967988898989786776666484455544436356446626542356542121
212353225632455544357554576775466484565886685899776676678767999887988999977887786697876897877586669859884576568856734465534364235245665625141
333524254566355353744477347456748466848486895578685898877666778699797799897798787966979678786787596577644845565687673555436765345562243453131
532453436656423432367774656354888887764868676575687789996779777667998887799999869766768798997969798875566577558768775655345754455532545545525
141414236635343346374764777677776578674467888555568789868788786777799999987977799796797996886875888797955757544578367476353752326465646614241
122335243622234566336666556548487477846645885989777976796688788999996666766969896876997976898998868655756575448874473574356666632462232242241
554443366643565466246576465773565747848566566689959696969666999888878869787666697677878879566677566566777468566566464663556353554432236353334
411511556322344646247744635753576484644847796998775677696799976888779789669679876767698675797986678856655864685674377735457443262355522114411
455443235465652464456734435566885646855554775575776865567766676867866697778969778798698665758969589998854665665863674535555562455356434331422
121245312663356425265447676537355445447748788997795986857888968668979966869776788869897666777878675865687447557666577553476524236545435431523
512152555326265363623746775744667444475767559996967689576796688789788787879988697868685755779565966765757885784477366564536344235353624134424
234424515426254554354664367354677686568446586555688896856667869779788876967686878696769859988857655784858668676457774453754524532454643345254
545153543365463242335355675774577444644646677989889587665666797699787969697889688796567787697695667644845768745677354636634334523532261321323
112113214343443336542743344467635685855677655767688676965976569788887887689768897979595796675876787674574555475655676774345662243334525523535
131325424436226645262465655375647864767768785455987575577665556879766869769786669679957978776788766487675586557557545347433455432363254225552
123515344352423236626335756775543758855685564456895697698655879987879687686677897577985559597658747676888876873447337545642465334623611151155
341124122166456665242355657353333456477675655859887958586757878679679878855589596778979659795775478577478875744537764376354544362542412131211
114222523344463642452533657747445545458764677555588687686867675796598776586695659959777976765788445657744765367556557677636245356653455133513
352255321212456234335456445433436355766847454767499597859958665989877785778869757886688885658684656587884587346443565337452654623566313342544
242415551213546266624526444745344364774688458487464587997759695967666576789769587999596756654647577488556745554545467737253366242452234113454
443131554335646424535333365475733655766854485764574678799569967769985889868959665889867858768474465754755767344464377675625453656664432453143
533252112413422535665233565734673564456787684576754556969556566687897999887985898667889798687556885754765746665474667373562525235265152251251
352511515133254633366436347336546733464778674684456584769656956696966959878589866888576564684457558468674373376677544466366655253442214122235
314153534535235666336266244443347774766854844887485554466857989767598999885555958958758875588858856758485446374645757246532524526435533325224
322435142422434426235362534357757336535774676778667547455686567856968786955566996778777775645865586786567336457667535636533666323451232535311
142254412124133652356265523754353474753538654476488677564875487959888685857759899566747787465584748664374454757474444563243553243423535521553
341424443342331354552224633536464356374543874867774457745477455468968677888678877466857447545754564566547475754647655253552626663453443332533
224424534541344325526464566266437476736775448557556474484485646874745446886586458878464468444757747444755346735763642232336644233345355251431
443112135411124246546345626223664637655433435655675864775786755766548866748764844644777786448864477366336545336763466345466446252522214251141
133325315324231452264622633266664754546545775647575487555666574444848475766785585686876485574755764733647757364543526232444454351245443254213
314131521225133215364666245353645737777744635736688644455487744588665485877488464574456674887784437574454377665723643366363453325532551531141
324344535551353354553523624554353575536465645357576768567567865556677665776487885665554776865744355453567434335566633325246333544411531123444
213111233544114452424345662455353743574535645456777888774866577758747788577855585656878458667773777553433533333626253335565412314222341343224
234443353422121552122655663324522656544546663775375585567866746466768887767485747746785747734475357336365645762522224532653414421514122321234
222123414512121142344523262624466255665443665546537347565766588857857885764466645677487876473355577537755433622563325264646541314211551313413
444243143445353251221553562665255246563755544553756556663656886858874547544886678474545675454455436574556436326464632326635425255351145111442
232212445333144123443545454454645235545654377634647635435566686757868658746845647465354645534537575455376533462364254663521131451114424242131
241434334451455421433323323664436433223565344634365356646575664447775668584446657764445344474337675643335234556645243626355115323144142231123
244443434514425512352325326265246226352465536436365536674474445433774744367776553356634463346366747646662662253542642263552351153443414324432
433233323232153553345112336433335563253456447444544743757677473663745665574346746434646363364636435377523422334644432652553414551222512114421
232322331233121424554252526264646466663336437465665756375455533373776465466433333446363764464637456522444454562433243334253355123315224312143
133313322332122441412111333654626643563564446544633464546367536547673537674334375565455775565444677245352453444263325413215252111352113324244
414434143343221114253331425436524563645433546467735774443733736573737434734363656553377447345646432263435434236365421152114552334511334444311
243223222431114215255542113356245526225262563443554664376773466467645336666377534536743756674533646256425462462562423131154445521142414113334
243434312424124113343141224334356622524233533343233663656343464335636757636754553764467776346562324463424443665241522124345534452221111321334
211414234122141132234253312111264245236344663655222237443544436737775344354755766473566567445662364655366235652213415435534211412142244114434
332224132332241152441323151335226464345324526555542555257443367365764333434753674467735364332336446466244323452231223133434231442123434313442
111214424144312345132212351425232545434436266463422643446342764447664675777457735742532253635532266633363425225433112221545532441213323124221
111442321412343431253224134241152223633622336344425445625535634256563777457372643426455424633524545262543244133534551554434324111123311211113
233313311143343143351431455251345111352234564443566663536246242462356525465634354423344225554636663262633335352323213242341221142244131323421
111121243444434421131134112523111542115455644535633444325664652666625635523322255264625564252255665243425424225133352415144121222223442423132
131321313144343423121433433145141525552365534452555456242343665525432352356624326235446254365452344244322243551113251432153344222334143141113
311113131433233332234114315415142312242514432264564632332532262334445245556434425656244562464362642622553325351433232435314233213122331231121
131311334423133434213414435222453532244233224636525564222254526456533636366634426563534323553336226114251341512421333242421244332313241132321
322211312341442332424212355325125152245543412546266662223634434552555354443546246246645254234425223445424144225225221513332423242121322231211
122211313233314122422143224214253441114334215451265434536455345256364565264365436434634323265521353523542253242112315342212223214433223312231
122222312224143314231134444525315141331224534322121665562342636234255324243362255634253654525144354453214243144424251324233141114312312332311
113321233111343212344241143344444125353442224245214151164446344566336426664262465536233552535341211413411251344223131122124134144223331221132
223223121222331122413122432214121535353511552152521441344232245253236453244353345534224211555145311345444311331534224432441422111132123131331
113321131313314243244322112423211123543333431242251531321351351221462565253244145552322223115433314234552323555241141111431314131333313121211
312323323221121344212442341132423323411341444542554342354351555354555452232354212452354235435223335421544531342322132422433423212322213312121
332321113311133314331343333442424143355521452552312223212432512325123114511223513412511334525513424325151424444413131433131142312131123321221
133213311222132133222241111144212411415135124431343111354114512341524254542254152431531154243344351253254314222444442131423241113233312322233
122233332221321332334332421112231241231454155421253323413131135544412332231134255525322253113541241522413343332322132232122322331232132222321""".split('\n')

Input=[[int(char) for char in line] for line in Input]
# print(Input, '\n')

# Enter : Top-left corner
# Arrival : Bottom-right corner
# Constraints : 
#   Can go straight more than 3 blocs (more than 3 case having same direction)
#   Can NOT go back


len_hor = len(Input[0])
len_ver = len(Input)
Map_Full = Graph()

max_dist = 3

"""
# From Map_Right | Right : 0-99999
for h in range(len_ver):
    for i in range(len_hor-3):
        # To Map_Top
        Map_Full.add_edge(h*(len_hor) + i, h*(len_hor)+i+1 + 200000, Input[h][i+1])
        Map_Full.add_edge(h*(len_hor) + i, h*(len_hor)+i+2 + 200000, sum([Input[h][i+1], Input[h][i+2]]))
        Map_Full.add_edge(h*(len_hor) + i, h*(len_hor)+i+3 + 200000, sum([Input[h][i+1], Input[h][i+2], Input[h][i+3]]))        

        # To Map_Bot
        Map_Full.add_edge(h*(len_hor) + i, h*(len_hor)+i+1 + 300000, Input[h][i+1])
        Map_Full.add_edge(h*(len_hor) + i, h*(len_hor)+i+2 + 300000, sum([Input[h][i+1], Input[h][i+2]]))
        Map_Full.add_edge(h*(len_hor) + i, h*(len_hor)+i+3 + 300000, sum([Input[h][i+1], Input[h][i+2], Input[h][i+3]]))   

    ## Special case for the last 2
    # To Map_Top
    Map_Full.add_edge(h*(len_hor) + len_hor-3, h*len_hor + len_hor -2 + 200000, Input[h][len_hor-2])
    Map_Full.add_edge(h*(len_hor) + len_hor-3, h*len_hor + len_hor -1 + 200000, sum([Input[h][len_hor-2], Input[h][len_hor-1]]))

    Map_Full.add_edge(h*(len_hor) + len_hor-2, h*len_hor + len_hor -1 + 200000, Input[h][len_hor-1])

    # To Map_Bot
    Map_Full.add_edge(h*(len_hor) + len_hor-3, h*len_hor + len_hor -2 + 300000, Input[h][len_hor-2])
    Map_Full.add_edge(h*(len_hor) + len_hor-3, h*len_hor + len_hor -1 + 300000, sum([Input[h][len_hor-2], Input[h][len_hor-1]]))

    Map_Full.add_edge(h*(len_hor) + len_hor-2, h*len_hor + len_hor -1 + 300000, Input[h][len_hor-1])

# From Map_Left | Left : 100000-199999
for h in range(len_ver):
    for i in range(3, len_hor):
        # To Map_Top | 200000-299999
        Map_Full.add_edge(h*len_hor + i + 100000, h*len_hor +i-1 + 200000, Input[h][i-1])
        Map_Full.add_edge(h*len_hor + i + 100000, h*len_hor +i-2 + 200000, sum([Input[h][i-1], Input[h][i-2]]))
        Map_Full.add_edge(h*len_hor + i + 100000, h*len_hor +i-3 + 200000, sum([Input[h][i-1], Input[h][i-2], Input[h][i-3]]))

        # To Map_Bot | 300000-399999
        Map_Full.add_edge(h*len_hor + i + 100000, h*len_hor +i-1 + 300000, Input[h][i-1])
        Map_Full.add_edge(h*len_hor + i + 100000, h*len_hor +i-2 + 300000, sum([Input[h][i-1], Input[h][i-2]]))
        Map_Full.add_edge(h*len_hor + i + 100000, h*len_hor +i-3 + 300000, sum([Input[h][i-1], Input[h][i-2], Input[h][i-3]]))

    ## Special case for the first 2
    # To Map_Top | 200000-299999
    Map_Full.add_edge(h*len_hor + 2 + 100000, h*len_hor +1 + 200000, Input[h][1])
    Map_Full.add_edge(h*len_hor + 2 + 100000, h*len_hor + 200000, sum([Input[h][1], Input[h][0]]))

    Map_Full.add_edge(h*len_hor + 1 + 100000, h*len_hor + 200000, Input[h][0])

    # To Map_Bot | 300000-399999
    Map_Full.add_edge(h*len_hor + 2 + 100000, h*len_hor +1 + 300000, Input[h][1])
    Map_Full.add_edge(h*len_hor + 2 + 100000, h*len_hor + 300000, sum([Input[h][1], Input[h][0]]))

    Map_Full.add_edge(h*len_hor + 1 + 100000, h*len_hor + 300000, Input[h][0])


# From Map_Top | Top : 200000-299999
for i in range(len_hor):
    for h in range(3, len_ver):
        # Top Map_Left | 100000-199999
        Map_Full.add_edge(h*(len_hor) + i + 200000, (h-1)*(len_hor)+i + 100000, Input[h-1][i])
        Map_Full.add_edge(h*(len_hor) + i + 200000, (h-2)*(len_hor)+i + 100000, sum([Input[h-1][i], Input[h-2][i]]))
        Map_Full.add_edge(h*(len_hor) + i + 200000, (h-3)*(len_hor)+i + 100000, sum([Input[h-1][i], Input[h-2][i], Input[h-3][i]]))

        # Top Map_Right | 0-9999
        Map_Full.add_edge(h*(len_hor) + i + 200000, (h-1)*(len_hor)+i, Input[h-1][i])
        Map_Full.add_edge(h*(len_hor) + i + 200000, (h-2)*(len_hor)+i, sum([Input[h-1][i], Input[h-2][i]]))
        Map_Full.add_edge(h*(len_hor) + i + 200000, (h-3)*(len_hor)+i, sum([Input[h-1][i], Input[h-2][i], Input[h-3][i]]))

    ## Special case for the last 2
    # To Map_Left | 100000-199999
    Map_Full.add_edge(2*len_hor + i + 200000, len_hor + i + 100000, Input[1][i])
    Map_Full.add_edge(2*len_hor + i + 200000, i + 100000, sum([Input[1][i], Input[0][i]]))

    Map_Full.add_edge(len_hor + i + 200000, i + 100000, Input[0][i])

    # To Map_Right | 0-99999
    Map_Full.add_edge(2*len_hor + i + 200000, len_hor + i, Input[1][i])
    Map_Full.add_edge(2*len_hor + i + 200000, i, sum([Input[1][i], Input[0][i]]))

    Map_Full.add_edge(len_hor + i + 200000, i, Input[0][i])


# Map_Bot | Bot : 300000-399999
for i in range(len_hor):
    for h in range(len_ver-3):
        # To Map_Left | 100000-199999
        Map_Full.add_edge(h*(len_hor) + i + 300000, (h+1)*(len_hor)+i + 100000, Input[h+1][i])
        Map_Full.add_edge(h*(len_hor) + i + 300000, (h+2)*(len_hor)+i + 100000, sum([Input[h+1][i], Input[h+2][i]]))
        Map_Full.add_edge(h*(len_hor) + i + 300000, (h+3)*(len_hor)+i + 100000, sum([Input[h+1][i], Input[h+2][i], Input[h+3][i]]))

        # To Map_Right | 0-9999
        Map_Full.add_edge(h*(len_hor) + i + 300000, (h+1)*(len_hor)+i, Input[h+1][i])
        Map_Full.add_edge(h*(len_hor) + i + 300000, (h+2)*(len_hor)+i, sum([Input[h+1][i], Input[h+2][i]]))
        Map_Full.add_edge(h*(len_hor) + i + 300000, (h+3)*(len_hor)+i, sum([Input[h+1][i], Input[h+2][i], Input[h+3][i]]))

    ## Special case for the last 2
    # To Map_Left | 100000-199999
    Map_Full.add_edge((len_ver-3)*len_hor + i + 300000, (len_ver-2)*len_hor + i + 100000, Input[len_ver-2][i])
    Map_Full.add_edge((len_ver-3)*len_hor + i + 300000, (len_ver-1)*len_hor + i + 100000, sum([Input[len_ver-2][i], Input[len_ver-1][i]]))

    Map_Full.add_edge((len_ver-2)*len_hor + i + 300000, (len_ver-1)*len_hor + i + 100000, Input[len_ver-1][i])

    # To Map_Right | 0-99999
    Map_Full.add_edge((len_ver-3)*len_hor + i + 300000, (len_ver-2)*len_hor + i, Input[len_ver-2][i])
    Map_Full.add_edge((len_ver-3)*len_hor + i + 300000, (len_ver-1)*len_hor + i, sum([Input[len_ver-2][i], Input[len_ver-1][i]]))

    Map_Full.add_edge((len_ver-2)*len_hor + i + 300000, (len_ver-1)*len_hor + i, Input[len_ver-1][i])

# Adding the two possible start (not including the initial value)
Map_Full.add_edge(999998, 0, 0)
Map_Full.add_edge(999998, 300000, 0)

# Adding the two path to end
Map_Full.add_edge(len_hor*len_ver - 1 + 0, 999999, 0)           # Coming from Map_Right
Map_Full.add_edge(len_hor*len_ver - 1 + 300000, 999999, 0)       # Coming from Map_Bot

print(f'This is supposedly the result : {find_path(Map_Full, 999998, 999999)} \n')                             # Start = 999998, End = 999999
"""

"""
Right : 0-99999
Left : 100000-199999
Top : 200000-299999
Bot : 300000-399999
"""

# Answer Part 1 : 684

### Part 2 

Map_Full2 = Graph()

# From Map_Right | Right : 0-9999
for h in range(len_ver):
    for i in range(len_hor-4):
        for Z in range(4, 11):
            if i+Z < len_hor:
                # To Map_Top | 20000-29999
                Map_Full2.add_edge(h*len_hor + i, h*len_hor +i+Z + 200000, sum(Input[h][i+1:i+Z+1]))
                # To Map_Bot | 30000-39999
                Map_Full2.add_edge(h*len_hor + i, h*len_hor +i+Z + 300000, sum(Input[h][i+1:i+Z+1]))


# From Map_Left | Left : 10000-19999
for h in range(len_ver):
    for i in range(4, len_hor):
        for Z in range(4, 11):
            if i-Z >= 0:        
                # To Map_Top | 20000-29999
                Map_Full2.add_edge(h*len_hor + i + 100000, h*len_hor +i-Z + 200000, sum(Input[h][i-Z:i]))
                # To Map_Bot | 30000-39999
                Map_Full2.add_edge(h*len_hor + i + 100000, h*len_hor +i-Z + 300000, sum(Input[h][i-Z:i]))

# From Map_Top | Top : 20000-29999
for i in range(len_hor):
    New_arr = [Input[_][i] for _ in range(len_ver)]
    for h in range(4, len_ver):
        for Z in range(4, 11):
            if h-Z >= 0:
                # Top Map_Left | 10000-19999
                Map_Full2.add_edge(h*len_hor + i + 200000, (h-Z)*(len_hor)+i + 100000, sum(New_arr[h-Z:h]))
                # Top Map_Right | 0-9999
                Map_Full2.add_edge(h*len_hor + i + 200000, (h-Z)*(len_hor)+i, sum(New_arr[h-Z:h]))


# From Map_Bot | Bot : 30000-39999
for i in range(len_hor):
    New_arr = [Input[_][i] for _ in range(len_ver)]
    for h in range(len_ver-4):
        for Z in range(4, 11):
            if h+Z < len_ver:
                # To Map_Left | 10000-19999
                Map_Full2.add_edge(h*len_hor + i + 300000, (h+Z)*(len_hor)+i + 100000, sum(New_arr[h+1:h+Z+1]))
                # To Map_Right | 0-9999
                Map_Full2.add_edge(h*len_hor + i + 300000, (h+Z)*(len_hor)+i, sum(New_arr[h+1:h+Z+1]))

print("All maps were created !")

# Adding the two possible start (not including the initial value)
Map_Full2.add_edge(999998, 0, 0)
Map_Full2.add_edge(999998, 300000, 0)

# Adding the two path to end
Map_Full2.add_edge(len_hor*len_ver - 1 + 0, 999999, 0)               # Coming from Map_Right
Map_Full2.add_edge(len_hor*len_ver - 1 + 300000, 999999, 0)          # Coming from Map_Bot


print(f'This is supposedly the result : {find_path(Map_Full2, 999998, 999999)} \n')