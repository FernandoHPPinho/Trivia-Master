# -*- coding: utf-8 -*-
import json
import random

random.seed(7)

items = []

def add(qpt, qen, correct_pt, correct_en, d_pt, d_en):
    # d_pt and d_en must have exactly 3 items, same order/meaning
    idxs = list(range(4))
    random.shuffle(idxs)
    pool_pt = [correct_pt] + d_pt
    pool_en = [correct_en] + d_en
    opt_pt = [pool_pt[i] for i in idxs]
    opt_en = [pool_en[i] for i in idxs]
    answer = idxs.index(0)
    items.append((qpt, opt_pt, answer, qen, opt_en))

# --- Batch 1: independencia e formacao de nacoes ---
add("Em que ano o Brasil declarou independência de Portugal?", "In what year did Brazil declare independence from Portugal?",
    "1822", "1822", ["1808", "1889", "1500"], ["1808", "1889", "1500"])

add("Em que ano os Estados Unidos declararam independência da Grã-Bretanha?", "In what year did the United States declare independence from Great Britain?",
    "1776", "1776", ["1789", "1812", "1620"], ["1789", "1812", "1620"])

add("Em que ano a Índia conquistou independência do Reino Unido?", "In what year did India gain independence from the United Kingdom?",
    "1947", "1947", ["1930", "1950", "1965"], ["1930", "1950", "1965"])

add("Em que ano o Haiti se tornou independente da França?", "In what year did Haiti become independent from France?",
    "1804", "1804", ["1776", "1821", "1850"], ["1776", "1821", "1850"])

add("Em que ano o México conquistou independência da Espanha?", "In what year did Mexico gain independence from Spain?",
    "1821", "1821", ["1776", "1846", "1910"], ["1776", "1846", "1910"])

add("Em que ano a Argentina declarou independência da Espanha?", "In what year did Argentina declare independence from Spain?",
    "1816", "1816", ["1810", "1825", "1898"], ["1810", "1825", "1898"])

add("A Bolívia recebeu esse nome em homenagem a qual líder da independência sul-americana?", "Bolivia was named in honor of which leader of South American independence?",
    "Simón Bolívar", "Simón Bolívar", ["José de San Martín", "Bernardo O'Higgins", "Francisco de Miranda"], ["José de San Martín", "Bernardo O'Higgins", "Francisco de Miranda"])

add("Em que ano Cuba se tornou uma república independente?", "In what year did Cuba become an independent republic?",
    "1902", "1902", ["1898", "1959", "1920"], ["1898", "1959", "1920"])

add("Em que ano as Filipinas conquistaram independência dos Estados Unidos?", "In what year did the Philippines gain independence from the United States?",
    "1946", "1946", ["1935", "1898", "1960"], ["1935", "1898", "1960"])

add("Em que ano a Indonésia declarou independência?", "In what year did Indonesia declare independence?",
    "1945", "1945", ["1949", "1930", "1957"], ["1949", "1930", "1957"])

add("Em que ano o Vietnã declarou independência da França?", "In what year did Vietnam declare independence from France?",
    "1945", "1945", ["1954", "1975", "1930"], ["1954", "1975", "1930"])

add("Em que ano a Argélia conquistou independência da França?", "In what year did Algeria gain independence from France?",
    "1962", "1962", ["1956", "1970", "1945"], ["1956", "1970", "1945"])

add("Qual foi o primeiro país da África Subsaariana a conquistar independência do domínio colonial?", "Which was the first Sub-Saharan African country to gain independence from colonial rule?",
    "Gana", "Ghana", ["Nigéria", "Quênia", "África do Sul"], ["Nigeria", "Kenya", "South Africa"])

add("Em que ano a Nigéria conquistou independência do Reino Unido?", "In what year did Nigeria gain independence from the United Kingdom?",
    "1960", "1960", ["1957", "1963", "1975"], ["1957", "1963", "1975"])

add("Em que ano o Quênia conquistou independência do Reino Unido?", "In what year did Kenya gain independence from the United Kingdom?",
    "1963", "1963", ["1957", "1970", "1980"], ["1957", "1970", "1980"])

add("Qual é o país mais novo do mundo, reconhecido pela ONU em 2011?", "Which is the world's newest country, recognized by the UN in 2011?",
    "Sudão do Sul", "South Sudan", ["Timor-Leste", "Eritreia", "Kosovo"], ["Timor-Leste", "Eritrea", "Kosovo"])

add("Em que ano o Timor-Leste conquistou independência definitiva da Indonésia?", "In what year did Timor-Leste achieve definitive independence from Indonesia?",
    "2002", "2002", ["1975", "1999", "2010"], ["1975", "1999", "2010"])

add("A Eritreia conquistou independência de qual país em 1993?", "Eritrea gained independence from which country in 1993?",
    "Etiópia", "Ethiopia", ["Sudão", "Somália", "Egito"], ["Sudan", "Somalia", "Egypt"])

add("Em que ano Bangladesh se tornou independente do Paquistão?", "In what year did Bangladesh become independent from Pakistan?",
    "1971", "1971", ["1947", "1965", "1980"], ["1947", "1965", "1980"])

add("Em que ano Singapura se separou da Malásia e tornou-se independente?", "In what year did Singapore separate from Malaysia and become independent?",
    "1965", "1965", ["1957", "1971", "1980"], ["1957", "1971", "1980"])

add("Em que ano Angola conquistou independência de Portugal?", "In what year did Angola gain independence from Portugal?",
    "1975", "1975", ["1961", "1980", "1992"], ["1961", "1980", "1992"])

add("Em que ano Moçambique conquistou independência de Portugal?", "In what year did Mozambique gain independence from Portugal?",
    "1975", "1975", ["1961", "1980", "1990"], ["1961", "1980", "1990"])

add("O Panamá se separou de qual país em 1903, com apoio dos Estados Unidos?", "Panama separated from which country in 1903, with US support?",
    "Colômbia", "Colombia", ["Venezuela", "Equador", "Costa Rica"], ["Venezuela", "Ecuador", "Costa Rica"])

add("Em que ano a Austrália se tornou uma federação de colônias britânicas?", "In what year did Australia become a federation of British colonies?",
    "1901", "1901", ["1867", "1931", "1788"], ["1867", "1931", "1788"])

add("Em que ano foi formada a Confederação do Canadá?", "In what year was the Confederation of Canada formed?",
    "1867", "1867", ["1901", "1776", "1931"], ["1901", "1776", "1931"])

add("Em que ano o Estado de Israel foi proclamado?", "In what year was the State of Israel proclaimed?",
    "1948", "1948", ["1945", "1956", "1967"], ["1945", "1956", "1967"])

add("Em que ano o Paquistão se tornou independente da Índia britânica?", "In what year did Pakistan become independent from British India?",
    "1947", "1947", ["1950", "1940", "1971"], ["1950", "1940", "1971"])

add("Em que ano a União Soviética se dissolveu oficialmente?", "In what year did the Soviet Union officially dissolve?",
    "1991", "1991", ["1989", "1985", "1995"], ["1989", "1985", "1995"])

add("Em que ano a Alemanha foi reunificada?", "In what year was Germany reunified?",
    "1990", "1990", ["1989", "1991", "1985"], ["1989", "1991", "1985"])

add("Em que ano caiu o Muro de Berlim?", "In what year did the Berlin Wall fall?",
    "1989", "1989", ["1990", "1961", "1985"], ["1990", "1961", "1985"])

add("Em que ano o apartheid terminou na África do Sul, com Nelson Mandela eleito presidente?", "In what year did apartheid end in South Africa, with Nelson Mandela elected president?",
    "1994", "1994", ["1990", "1989", "2000"], ["1990", "1989", "2000"])

add("Em que ano Hong Kong foi devolvida à China pelo Reino Unido?", "In what year was Hong Kong returned to China by the United Kingdom?",
    "1997", "1997", ["1999", "1990", "2000"], ["1999", "1990", "2000"])

add("Em que ano Macau foi devolvida à China por Portugal?", "In what year was Macau returned to China by Portugal?",
    "1999", "1999", ["1997", "1987", "2000"], ["1997", "1987", "2000"])

add("A união entre Noruega e Suécia terminou pacificamente em que ano?", "The union between Norway and Sweden peacefully ended in what year?",
    "1905", "1905", ["1918", "1890", "1920"], ["1918", "1890", "1920"])

add("Em que ano a Finlândia declarou independência da Rússia?", "In what year did Finland declare independence from Russia?",
    "1917", "1917", ["1905", "1922", "1939"], ["1905", "1922", "1939"])

add("Em que ano a Islândia se tornou uma república independente da Dinamarca?", "In what year did Iceland become a republic independent from Denmark?",
    "1944", "1944", ["1918", "1930", "1950"], ["1918", "1930", "1950"])

add("Em que ano a Checoslováquia se dividiu pacificamente em República Tcheca e Eslováquia?", "In what year did Czechoslovakia peacefully split into the Czech Republic and Slovakia?",
    "1993", "1993", ["1989", "1991", "2000"], ["1989", "1991", "2000"])

add("Em que ano o Brasil se tornou uma república, encerrando o período monárquico?", "In what year did Brazil become a republic, ending the monarchical period?",
    "1889", "1889", ["1822", "1500", "1900"], ["1822", "1500", "1900"])

add("Em que ano Portugal se tornou uma república, encerrando a monarquia?", "In what year did Portugal become a republic, ending the monarchy?",
    "1910", "1910", ["1889", "1926", "1974"], ["1889", "1926", "1974"])

add("Em que ano ocorreu a Revolução Xinhai, que pôs fim ao império chinês?", "In what year did the Xinhai Revolution occur, ending the Chinese empire?",
    "1912", "1912", ["1949", "1900", "1925"], ["1949", "1900", "1925"])

add("Em que ano foi fundada a República Popular da China, sob liderança de Mao Zedong?", "In what year was the People's Republic of China founded, under Mao Zedong's leadership?",
    "1949", "1949", ["1945", "1912", "1959"], ["1945", "1912", "1959"])

add("Ao fim da Segunda Guerra Mundial, a Coreia foi dividida ao longo de qual paralelo?", "At the end of World War II, Korea was divided along which parallel?",
    "Paralelo 38", "38th parallel", ["Paralelo 45", "Paralelo 30", "Linha do Equador"], ["45th parallel", "30th parallel", "the Equator"])

add("Em que ano terminou a Guerra da Coreia com um armistício?", "In what year did the Korean War end with an armistice?",
    "1953", "1953", ["1950", "1960", "1945"], ["1950", "1960", "1945"])

add("Em que ano terminou a Guerra do Vietnã?", "In what year did the Vietnam War end?",
    "1975", "1975", ["1968", "1980", "1954"], ["1968", "1980", "1954"])

add("Em que ano Fidel Castro chegou ao poder após a Revolução Cubana?", "In what year did Fidel Castro come to power after the Cuban Revolution?",
    "1959", "1959", ["1953", "1962", "1970"], ["1953", "1962", "1970"])

# --- Batch 2: guerras, revolucoes, lideres e organizacoes ---
add("Em que ano começou a Primeira Guerra Mundial?", "In what year did World War I begin?",
    "1914", "1914", ["1918", "1939", "1905"], ["1918", "1939", "1905"])

add("Em que ano terminou a Primeira Guerra Mundial?", "In what year did World War I end?",
    "1918", "1918", ["1914", "1945", "1920"], ["1914", "1945", "1920"])

add("Em que ano começou a Segunda Guerra Mundial, com a invasão da Polônia?", "In what year did World War II begin, with the invasion of Poland?",
    "1939", "1939", ["1938", "1941", "1914"], ["1938", "1941", "1914"])

add("Em que ano terminou a Segunda Guerra Mundial?", "In what year did World War II end?",
    "1945", "1945", ["1944", "1939", "1950"], ["1944", "1939", "1950"])

add("Em que ano a bomba atômica foi lançada sobre Hiroshima?", "In what year was the atomic bomb dropped on Hiroshima?",
    "1945", "1945", ["1944", "1941", "1950"], ["1944", "1941", "1950"])

add("Quem foi o primeiro-ministro que liderou o Reino Unido durante a maior parte da Segunda Guerra Mundial?", "Who was the prime minister who led the United Kingdom for most of World War II?",
    "Winston Churchill", "Winston Churchill", ["Neville Chamberlain", "Clement Attlee", "Tony Blair"], ["Neville Chamberlain", "Clement Attlee", "Tony Blair"])

add("Quem foi o presidente dos Estados Unidos durante a maior parte da Segunda Guerra Mundial?", "Who was the President of the United States for most of World War II?",
    "Franklin D. Roosevelt", "Franklin D. Roosevelt", ["Harry Truman", "Woodrow Wilson", "Dwight Eisenhower"], ["Harry Truman", "Woodrow Wilson", "Dwight Eisenhower"])

add("Quem foi o líder da Alemanha nazista durante a Segunda Guerra Mundial?", "Who was the leader of Nazi Germany during World War II?",
    "Adolf Hitler", "Adolf Hitler", ["Otto von Bismarck", "Kaiser Wilhelm II", "Heinrich Himmler"], ["Otto von Bismarck", "Kaiser Wilhelm II", "Heinrich Himmler"])

add("Em que ano começou a Revolução Francesa?", "In what year did the French Revolution begin?",
    "1789", "1789", ["1799", "1776", "1804"], ["1799", "1776", "1804"])

add("Qual rei francês foi guilhotinado durante a Revolução Francesa?", "Which French king was guillotined during the French Revolution?",
    "Luís XVI", "Louis XVI", ["Luís XIV", "Napoleão", "Luís XV"], ["Louis XIV", "Napoleon", "Louis XV"])

add("Quem foi derrotado na Batalha de Waterloo, em 1815?", "Who was defeated at the Battle of Waterloo in 1815?",
    "Napoleão Bonaparte", "Napoleon Bonaparte", ["Luís XVI", "Otto von Bismarck", "Carlos Magno"], ["Louis XVI", "Otto von Bismarck", "Charlemagne"])

add("Quem liderou os bolcheviques na Revolução Russa de 1917?", "Who led the Bolsheviks in the 1917 Russian Revolution?",
    "Vladimir Lênin", "Vladimir Lenin", ["Josef Stalin", "Leon Trótski", "Nicolau II"], ["Joseph Stalin", "Leon Trotsky", "Nicholas II"])

add("Quem foi o líder da União Soviética durante a maior parte da Segunda Guerra Mundial?", "Who was the leader of the Soviet Union for most of World War II?",
    "Josef Stalin", "Joseph Stalin", ["Vladimir Lênin", "Nikita Khrushchov", "Leon Trótski"], ["Vladimir Lenin", "Nikita Khrushchev", "Leon Trotsky"])

add("Quem liderou o movimento de independência da Índia através da resistência pacífica?", "Who led India's independence movement through peaceful resistance?",
    "Mahatma Gandhi", "Mahatma Gandhi", ["Jawaharlal Nehru", "Muhammad Ali Jinnah", "Indira Gandhi"], ["Jawaharlal Nehru", "Muhammad Ali Jinnah", "Indira Gandhi"])

add("Quem foi o primeiro presidente dos Estados Unidos?", "Who was the first President of the United States?",
    "George Washington", "George Washington", ["Thomas Jefferson", "Abraham Lincoln", "John Adams"], ["Thomas Jefferson", "Abraham Lincoln", "John Adams"])

add("Quem foi o principal autor da Declaração de Independência dos Estados Unidos?", "Who was the principal author of the United States Declaration of Independence?",
    "Thomas Jefferson", "Thomas Jefferson", ["George Washington", "Benjamin Franklin", "James Madison"], ["George Washington", "Benjamin Franklin", "James Madison"])

add("Quem proclamou a independência do Brasil em 1822?", "Who proclaimed Brazil's independence in 1822?",
    "Dom Pedro I", "Dom Pedro I", ["Dom Pedro II", "Dom João VI", "Marquês de Pombal"], ["Dom Pedro II", "Dom João VI", "Marquis of Pombal"])

add("Quem foi o primeiro presidente eleito democraticamente da África do Sul pós-apartheid?", "Who was the first democratically elected president of post-apartheid South Africa?",
    "Nelson Mandela", "Nelson Mandela", ["Desmond Tutu", "Thabo Mbeki", "F.W. de Klerk"], ["Desmond Tutu", "Thabo Mbeki", "F.W. de Klerk"])

add("Em que ano foi fundada a Organização das Nações Unidas (ONU)?", "In what year was the United Nations (UN) founded?",
    "1945", "1945", ["1919", "1950", "1939"], ["1919", "1950", "1939"])

add("Em que cidade fica a sede da ONU?", "In which city is the UN headquarters located?",
    "Nova York", "New York", ["Genebra", "Bruxelas", "Haia"], ["Geneva", "Brussels", "The Hague"])

add("Qual organização internacional precedeu a ONU, criada após a Primeira Guerra Mundial?", "Which international organization preceded the UN, created after World War I?",
    "Liga das Nações", "League of Nations", ["OTAN", "União Europeia", "G7"], ["NATO", "European Union", "G7"])

add("Em que cidade fica a sede da Comissão Europeia, principal órgão executivo da União Europeia?", "In which city is the European Commission, the EU's main executive body, headquartered?",
    "Bruxelas", "Brussels", ["Paris", "Estrasburgo", "Genebra"], ["Paris", "Strasbourg", "Geneva"])

add("Quantos países fundaram originalmente a Comunidade Econômica Europeia em 1957?", "How many countries originally founded the European Economic Community in 1957?",
    "Seis", "Six", ["Quatro", "Nove", "Doze"], ["Four", "Nine", "Twelve"])

add("Em que ano foi assinado o Tratado de Maastricht, que criou formalmente a União Europeia?", "In what year was the Maastricht Treaty signed, formally creating the European Union?",
    "1993", "1993", ["1957", "1999", "2000"], ["1957", "1999", "2000"])

add("Qual país deixou a União Europeia em 2020, no processo conhecido como Brexit?", "Which country left the European Union in 2020, in the process known as Brexit?",
    "Reino Unido", "United Kingdom", ["Irlanda", "Noruega", "Suíça"], ["Ireland", "Norway", "Switzerland"])

add("Em que ano foi fundada a OTAN (Organização do Tratado do Atlântico Norte)?", "In what year was NATO (North Atlantic Treaty Organization) founded?",
    "1949", "1949", ["1945", "1955", "1961"], ["1945", "1955", "1961"])

add("Quais quatro países fundaram originalmente o Mercosul, em 1991?", "Which four countries originally founded Mercosur, in 1991?",
    "Brasil, Argentina, Paraguai e Uruguai", "Brazil, Argentina, Paraguay and Uruguay", ["Brasil, Chile, Peru e Bolívia", "Brasil, Colômbia, Venezuela e México", "Argentina, Chile, Uruguai e Bolívia"], ["Brazil, Chile, Peru and Bolivia", "Brazil, Colombia, Venezuela and Mexico", "Argentina, Chile, Uruguay and Bolivia"])

add("Quantos membros permanentes com poder de veto tem o Conselho de Segurança da ONU?", "How many permanent members with veto power does the UN Security Council have?",
    "Cinco", "Five", ["Três", "Sete", "Dez"], ["Three", "Seven", "Ten"])

add("Qual destes NÃO é membro permanente do Conselho de Segurança da ONU?", "Which of these is NOT a permanent member of the UN Security Council?",
    "Alemanha", "Germany", ["Estados Unidos", "China", "Rússia"], ["United States", "China", "Russia"])

add("Qual é a moeda oficial da maioria dos países da União Europeia?", "What is the official currency of most European Union countries?",
    "Euro", "Euro", ["Libra esterlina", "Franco", "Marco"], ["Pound sterling", "Franc", "Mark"])

add("Qual organização de comércio mundial foi fundada em 1995, sucedendo o GATT?", "Which world trade organization was founded in 1995, succeeding GATT?",
    "Organização Mundial do Comércio (OMC)", "World Trade Organization (WTO)", ["Fundo Monetário Internacional", "Banco Mundial", "G20"], ["International Monetary Fund", "World Bank", "G20"])

add("Em que cidade fica a sede do Fundo Monetário Internacional (FMI)?", "In which city is the International Monetary Fund (IMF) headquartered?",
    "Washington, D.C.", "Washington, D.C.", ["Nova York", "Genebra", "Paris"], ["New York", "Geneva", "Paris"])

add("Qual é a forma de governo em que o poder é herdado por uma família real?", "What form of government is one in which power is inherited by a royal family?",
    "Monarquia", "Monarchy", ["República", "Democracia direta", "Teocracia"], ["Republic", "Direct democracy", "Theocracy"])

add("Qual destes países é uma monarquia constitucional atualmente?", "Which of these countries is currently a constitutional monarchy?",
    "Japão", "Japan", ["França", "Estados Unidos", "Brasil"], ["France", "United States", "Brazil"])

add("Qual destes países é uma monarquia constitucional na Europa?", "Which of these countries is a constitutional monarchy in Europe?",
    "Suécia", "Sweden", ["Alemanha", "França", "Itália"], ["Germany", "France", "Italy"])

add("Como se chama o sistema de governo dos Estados Unidos, dividido em Executivo, Legislativo e Judiciário?", "What is the name of the US system of government, divided into Executive, Legislative and Judiciary?",
    "Presidencialismo", "Presidential system", ["Parlamentarismo", "Monarquia constitucional", "Confederalismo"], ["Parliamentary system", "Constitutional monarchy", "Confederalism"])

add("No parlamentarismo, quem geralmente é o chefe de governo?", "In a parliamentary system, who is usually the head of government?",
    "O primeiro-ministro", "The prime minister", ["O presidente", "O rei", "O chanceler militar"], ["The president", "The king", "The military chancellor"])

add("Qual cidade-estado do Vaticano é governada por qual líder religioso e político?", "The Vatican City-state is governed by which religious and political leader?",
    "O Papa", "The Pope", ["O Patriarca", "O Cardeal-decano", "O Rei"], ["The Patriarch", "The Dean of Cardinals", "The King"])

add("Qual é o nome do parlamento do Reino Unido?", "What is the name of the United Kingdom's parliament?",
    "Westminster", "Westminster", ["Bundestag", "Assembleia Nacional", "Congresso"], ["Bundestag", "National Assembly", "Congress"])

add("Qual é o nome do parlamento da Alemanha?", "What is the name of Germany's parliament?",
    "Bundestag", "Bundestag", ["Westminster", "Senado", "Duma"], ["Westminster", "Senate", "Duma"])

add("Qual é o nome do parlamento da Rússia (câmara baixa)?", "What is the name of Russia's parliament (lower house)?",
    "Duma", "Duma", ["Bundestag", "Knesset", "Senado"], ["Bundestag", "Knesset", "Senate"])

add("Qual é o nome do parlamento de Israel?", "What is the name of Israel's parliament?",
    "Knesset", "Knesset", ["Duma", "Majlis", "Diwan"], ["Duma", "Majlis", "Diwan"])

# --- Batch 3: patrimonios, monumentos e marcos culturais ---
add("Em que país está localizada a Torre Eiffel?", "In which country is the Eiffel Tower located?",
    "França", "France", ["Itália", "Espanha", "Bélgica"], ["Italy", "Spain", "Belgium"])

add("Em que país está localizado o Coliseu?", "In which country is the Colosseum located?",
    "Itália", "Italy", ["Grécia", "França", "Turquia"], ["Greece", "France", "Turkey"])

add("Em que país está localizada a Grande Muralha?", "In which country is the Great Wall located?",
    "China", "China", ["Mongólia", "Japão", "Coreia do Sul"], ["Mongolia", "Japan", "South Korea"])

add("Em que país está localizado o Taj Mahal?", "In which country is the Taj Mahal located?",
    "Índia", "India", ["Paquistão", "Bangladesh", "Nepal"], ["Pakistan", "Bangladesh", "Nepal"])

add("Em que país está localizado Machu Picchu?", "In which country is Machu Picchu located?",
    "Peru", "Peru", ["Bolívia", "Equador", "Chile"], ["Bolivia", "Ecuador", "Chile"])

add("Em que país está localizada a estátua do Cristo Redentor?", "In which country is the Christ the Redeemer statue located?",
    "Brasil", "Brazil", ["Argentina", "Portugal", "México"], ["Argentina", "Portugal", "Mexico"])

add("Em que país estão localizadas as pirâmides de Gizé?", "In which country are the pyramids of Giza located?",
    "Egito", "Egypt", ["Sudão", "Líbia", "Iraque"], ["Sudan", "Libya", "Iraq"])

add("Em que país está localizada Petra, a cidade esculpida na rocha?", "In which country is Petra, the city carved into rock, located?",
    "Jordânia", "Jordan", ["Egito", "Síria", "Líbano"], ["Egypt", "Syria", "Lebanon"])

add("Em que país está localizado Stonehenge?", "In which country is Stonehenge located?",
    "Reino Unido", "United Kingdom", ["Irlanda", "França", "Escócia (fora do Reino Unido)"], ["Ireland", "France", "Scotland (outside the UK)"])

add("Em que país está localizada a cidade de Angkor Wat?", "In which country is the city of Angkor Wat located?",
    "Camboja", "Cambodia", ["Tailândia", "Vietnã", "Laos"], ["Thailand", "Vietnam", "Laos"])

add("Em que país está localizada a Acrópole de Atenas?", "In which country is the Acropolis of Athens located?",
    "Grécia", "Greece", ["Itália", "Turquia", "Chipre"], ["Italy", "Turkey", "Cyprus"])

add("Qual organização da ONU é responsável por listar Patrimônios Mundiais da Humanidade?", "Which UN organization is responsible for listing World Heritage Sites?",
    "UNESCO", "UNESCO", ["UNICEF", "OMS", "FAO"], ["UNICEF", "WHO", "FAO"])

add("Em que país está localizado o Vale dos Reis, com tumbas de faraós?", "In which country is the Valley of the Kings, with pharaoh tombs, located?",
    "Egito", "Egypt", ["Sudão", "Etiópia", "Jordânia"], ["Sudan", "Ethiopia", "Jordan"])

add("Em que país está localizada a cidade histórica de Cartago?", "In which country is the historic city of Carthage located?",
    "Tunísia", "Tunisia", ["Marrocos", "Líbia", "Argélia"], ["Morocco", "Libya", "Algeria"])

add("Em que país fica o Kremlin?", "In which country is the Kremlin located?",
    "Rússia", "Russia", ["Ucrânia", "Bielorrússia", "Polônia"], ["Ukraine", "Belarus", "Poland"])

add("Em que país está localizada a Sagrada Família, obra de Gaudí?", "In which country is the Sagrada Família, a work by Gaudí, located?",
    "Espanha", "Spain", ["Portugal", "Itália", "França"], ["Portugal", "Italy", "France"])

add("Em que país está localizado o Big Ben?", "In which country is Big Ben located?",
    "Reino Unido", "United Kingdom", ["Irlanda", "França", "Alemanha"], ["Ireland", "France", "Germany"])

add("Em que país está localizada a Estátua da Liberdade?", "In which country is the Statue of Liberty located?",
    "Estados Unidos", "United States", ["Canadá", "França", "México"], ["Canada", "France", "Mexico"])

add("A Estátua da Liberdade foi um presente de qual país aos Estados Unidos?", "The Statue of Liberty was a gift from which country to the United States?",
    "França", "France", ["Reino Unido", "Espanha", "Itália"], ["United Kingdom", "Spain", "Italy"])

add("Em que país está localizado o Deserto do Saara em sua maior parte?", "In which region is most of the Sahara Desert located?",
    "Norte da África", "North Africa", ["Oriente Médio", "Ásia Central", "África Austral"], ["Middle East", "Central Asia", "Southern Africa"])

add("Qual é o maior deserto de areia quente do mundo?", "What is the largest hot sand desert in the world?",
    "Saara", "Sahara", ["Gobi", "Atacama", "Kalahari"], ["Gobi", "Atacama", "Kalahari"])

add("Em que continente fica o Deserto do Atacama, um dos mais secos do mundo?", "On which continent is the Atacama Desert, one of the driest in the world, located?",
    "América do Sul", "South America", ["África", "Ásia", "Oceania"], ["Africa", "Asia", "Oceania"])

add("Qual é o rio mais longo do mundo?", "What is the longest river in the world?",
    "Nilo", "Nile", ["Amazonas", "Mississippi", "Yangtzé"], ["Amazon", "Mississippi", "Yangtze"])

add("Qual é a maior floresta tropical do mundo?", "What is the largest rainforest in the world?",
    "Floresta Amazônica", "Amazon Rainforest", ["Floresta do Congo", "Floresta Boreal", "Selva de Bornéu"], ["Congo Rainforest", "Boreal Forest", "Borneo Rainforest"])

add("Qual é a cadeia de montanhas mais alta do mundo?", "What is the highest mountain range in the world?",
    "Himalaia", "Himalayas", ["Andes", "Alpes", "Rochosas"], ["Andes", "Alps", "Rockies"])

add("Em qual cordilheira está localizado o Monte Everest?", "In which mountain range is Mount Everest located?",
    "Himalaia", "Himalayas", ["Andes", "Alpes", "Cáucaso"], ["Andes", "Alps", "Caucasus"])

add("Qual é o maior país do mundo em extensão territorial?", "What is the largest country in the world by land area?",
    "Rússia", "Russia", ["Canadá", "China", "Estados Unidos"], ["Canada", "China", "United States"])

add("Qual é o menor país do mundo em extensão territorial?", "What is the smallest country in the world by land area?",
    "Vaticano", "Vatican City", ["Mônaco", "San Marino", "Liechtenstein"], ["Monaco", "San Marino", "Liechtenstein"])

add("Qual é o país mais populoso do mundo atualmente?", "Which is currently the most populous country in the world?",
    "Índia", "India", ["China", "Estados Unidos", "Indonésia"], ["China", "United States", "Indonesia"])

# --- Batch 4: arte, literatura e premios Nobel ---
add("Quem pintou a Mona Lisa?", "Who painted the Mona Lisa?",
    "Leonardo da Vinci", "Leonardo da Vinci", ["Michelangelo", "Rafael", "Botticelli"], ["Michelangelo", "Raphael", "Botticelli"])

add("Quem pintou o teto da Capela Sistina?", "Who painted the ceiling of the Sistine Chapel?",
    "Michelangelo", "Michelangelo", ["Leonardo da Vinci", "Rafael", "Donatello"], ["Leonardo da Vinci", "Raphael", "Donatello"])

add("Qual pintor espanhol é conhecido por obras como Guernica?", "Which Spanish painter is known for works such as Guernica?",
    "Pablo Picasso", "Pablo Picasso", ["Salvador Dalí", "Diego Velázquez", "Francisco Goya"], ["Salvador Dalí", "Diego Velázquez", "Francisco Goya"])

add("Qual pintor holandês é famoso por 'A Noite Estrelada' e cortou a própria orelha?", "Which Dutch painter is famous for 'The Starry Night' and cut off his own ear?",
    "Vincent van Gogh", "Vincent van Gogh", ["Rembrandt", "Johannes Vermeer", "Piet Mondrian"], ["Rembrandt", "Johannes Vermeer", "Piet Mondrian"])

add("Qual escritor inglês escreveu 'Romeu e Julieta' e 'Hamlet'?", "Which English writer wrote 'Romeo and Juliet' and 'Hamlet'?",
    "William Shakespeare", "William Shakespeare", ["Charles Dickens", "Jane Austen", "Oscar Wilde"], ["Charles Dickens", "Jane Austen", "Oscar Wilde"])

add("Qual escritor brasileiro escreveu 'Dom Casmurro' e 'Memórias Póstumas de Brás Cubas'?", "Which Brazilian writer wrote 'Dom Casmurro' and 'The Posthumous Memoirs of Brás Cubas'?",
    "Machado de Assis", "Machado de Assis", ["Jorge Amado", "Carlos Drummond de Andrade", "Guimarães Rosa"], ["Jorge Amado", "Carlos Drummond de Andrade", "Guimarães Rosa"])

add("Qual escritor colombiano escreveu 'Cem Anos de Solidão' e ganhou o Nobel de Literatura?", "Which Colombian writer wrote 'One Hundred Years of Solitude' and won the Nobel Prize in Literature?",
    "Gabriel García Márquez", "Gabriel García Márquez", ["Mario Vargas Llosa", "Pablo Neruda", "Jorge Luis Borges"], ["Mario Vargas Llosa", "Pablo Neruda", "Jorge Luis Borges"])

add("Qual escritor russo escreveu 'Guerra e Paz'?", "Which Russian writer wrote 'War and Peace'?",
    "Liev Tolstói", "Leo Tolstoy", ["Fiódor Dostoiévski", "Anton Tchekhov", "Aleksandr Púchkin"], ["Fyodor Dostoevsky", "Anton Chekhov", "Alexander Pushkin"])

add("Quem escreveu a saga de fantasia 'O Senhor dos Anéis'?", "Who wrote the fantasy saga 'The Lord of the Rings'?",
    "J.R.R. Tolkien", "J.R.R. Tolkien", ["C.S. Lewis", "George R.R. Martin", "J.K. Rowling"], ["C.S. Lewis", "George R.R. Martin", "J.K. Rowling"])

add("Qual prêmio é considerado a mais alta honraria mundial em áreas como literatura, paz e ciências?", "Which prize is considered the world's highest honor in fields like literature, peace and the sciences?",
    "Prêmio Nobel", "Nobel Prize", ["Prêmio Pulitzer", "Medalha Fields", "Prêmio Turing"], ["Pulitzer Prize", "Fields Medal", "Turing Award"])

add("Em qual país o Prêmio Nobel da Paz é entregue, diferente dos demais prêmios Nobel?", "In which country is the Nobel Peace Prize awarded, unlike the other Nobel prizes?",
    "Noruega", "Norway", ["Suécia", "Dinamarca", "Suíça"], ["Sweden", "Denmark", "Switzerland"])

add("Em qual cidade a maioria dos Prêmios Nobel é entregue anualmente?", "In which city are most Nobel Prizes awarded annually?",
    "Estocolmo", "Stockholm", ["Oslo", "Genebra", "Copenhague"], ["Oslo", "Geneva", "Copenhagen"])

add("Quem foi o cientista alemão que desenvolveu a teoria da relatividade?", "Who was the German scientist who developed the theory of relativity?",
    "Albert Einstein", "Albert Einstein", ["Isaac Newton", "Niels Bohr", "Max Planck"], ["Isaac Newton", "Niels Bohr", "Max Planck"])

add("Quem foi a cientista polonesa-francesa pioneira em radioatividade, ganhadora de dois Prêmios Nobel?", "Who was the Polish-French scientist who pioneered radioactivity research and won two Nobel Prizes?",
    "Marie Curie", "Marie Curie", ["Rosalind Franklin", "Ada Lovelace", "Lise Meitner"], ["Rosalind Franklin", "Ada Lovelace", "Lise Meitner"])

add("Qual compositor alemão, que ficou surdo, escreveu a Nona Sinfonia?", "Which German composer, who became deaf, wrote the Ninth Symphony?",
    "Ludwig van Beethoven", "Ludwig van Beethoven", ["Johann Sebastian Bach", "Wolfgang Amadeus Mozart", "Johannes Brahms"], ["Johann Sebastian Bach", "Wolfgang Amadeus Mozart", "Johannes Brahms"])

add("Qual compositor austríaco foi considerado um prodígio musical desde criança, autor de 'A Flauta Mágica'?", "Which Austrian composer was considered a musical prodigy from childhood, author of 'The Magic Flute'?",
    "Wolfgang Amadeus Mozart", "Wolfgang Amadeus Mozart", ["Ludwig van Beethoven", "Franz Schubert", "Joseph Haydn"], ["Ludwig van Beethoven", "Franz Schubert", "Joseph Haydn"])

add("Qual grupo musical britânico dos anos 1960, formado por John Lennon e Paul McCartney, é um dos mais influentes da história?", "Which British 1960s band, formed by John Lennon and Paul McCartney, is one of the most influential in history?",
    "The Beatles", "The Beatles", ["The Rolling Stones", "Pink Floyd", "Queen"], ["The Rolling Stones", "Pink Floyd", "Queen"])

add("Qual estilo musical, com raízes afro-americanas, é considerado a base do rock e do pop moderno?", "Which musical style, with African-American roots, is considered the foundation of modern rock and pop?",
    "Blues", "Blues", ["Ópera", "Música clássica", "Fado"], ["Opera", "Classical music", "Fado"])

add("O tango é uma dança e estilo musical tradicionalmente associado a qual país?", "Tango is a dance and musical style traditionally associated with which country?",
    "Argentina", "Argentina", ["Brasil", "México", "Espanha"], ["Brazil", "Mexico", "Spain"])

add("O flamenco é uma dança e estilo musical tradicional de qual país?", "Flamenco is a traditional dance and musical style from which country?",
    "Espanha", "Spain", ["Portugal", "Itália", "México"], ["Portugal", "Italy", "Mexico"])

add("O samba é um gênero musical e dança tradicionalmente associado a qual país?", "Samba is a musical genre and dance traditionally associated with which country?",
    "Brasil", "Brazil", ["Cuba", "Colômbia", "Portugal"], ["Cuba", "Colombia", "Portugal"])

add("O fado é um gênero musical melancólico tradicional de qual país?", "Fado is a traditional melancholic musical genre from which country?",
    "Portugal", "Portugal", ["Espanha", "Itália", "Grécia"], ["Spain", "Italy", "Greece"])

# --- Batch 5: festas, tradicoes, culinaria e mitologia ---
add("O Carnaval é celebrado com grande destaque em qual cidade brasileira, famosa por seu desfile de escolas de samba?", "Carnival is celebrated prominently in which Brazilian city, famous for its samba school parade?",
    "Rio de Janeiro", "Rio de Janeiro", ["São Paulo", "Brasília", "Salvador (menos famoso pelo desfile)"], ["São Paulo", "Brasília", "Salvador (less famous for the parade)"])

add("A Oktoberfest, grande festival de cerveja, se originou em qual país?", "Oktoberfest, the major beer festival, originated in which country?",
    "Alemanha", "Germany", ["Áustria", "Bélgica", "Holanda"], ["Austria", "Belgium", "Netherlands"])

add("O Dia dos Mortos (Día de los Muertos) é uma celebração tradicional de qual país?", "Day of the Dead (Día de los Muertos) is a traditional celebration in which country?",
    "México", "Mexico", ["Espanha", "Peru", "Guatemala"], ["Spain", "Peru", "Guatemala"])

add("O Diwali, conhecido como o 'festival das luzes', é celebrado principalmente por qual religião/cultura?", "Diwali, known as the 'festival of lights', is mainly celebrated by which religion/culture?",
    "Hinduísmo (Índia)", "Hinduism (India)", ["Budismo (Tailândia)", "Islamismo (Indonésia)", "Xintoísmo (Japão)"], ["Buddhism (Thailand)", "Islam (Indonesia)", "Shinto (Japan)"])

add("O Songkran, festival de ano novo com brincadeiras de água, é celebrado em qual país?", "Songkran, a new year festival with water celebrations, is celebrated in which country?",
    "Tailândia", "Thailand", ["Vietnã", "Camboja", "Filipinas"], ["Vietnam", "Cambodia", "Philippines"])

add("A festa de La Tomatina, onde participantes se atiram tomates, acontece em qual país?", "The La Tomatina festival, where participants throw tomatoes at each other, takes place in which country?",
    "Espanha", "Spain", ["Itália", "México", "Portugal"], ["Italy", "Mexico", "Portugal"])

add("Qual prato é considerado o prato nacional do Brasil, feito com feijão preto e carnes?", "Which dish is considered Brazil's national dish, made with black beans and meats?",
    "Feijoada", "Feijoada", ["Moqueca", "Churrasco", "Vatapá"], ["Moqueca", "Churrasco", "Vatapá"])

add("A paella é um prato tradicional de qual país?", "Paella is a traditional dish from which country?",
    "Espanha", "Spain", ["Itália", "Portugal", "Marrocos"], ["Italy", "Portugal", "Morocco"])

add("O sushi é um prato tradicional de qual país?", "Sushi is a traditional dish from which country?",
    "Japão", "Japan", ["China", "Coreia do Sul", "Tailândia"], ["China", "South Korea", "Thailand"])

add("O curry é um prato fortemente associado à culinária de qual país?", "Curry is a dish strongly associated with which country's cuisine?",
    "Índia", "India", ["China", "Tailândia", "Indonésia"], ["China", "Thailand", "Indonesia"])

add("A pizza margherita, com molho, mussarela e manjericão, é originária de qual país?", "Margherita pizza, with sauce, mozzarella and basil, originated in which country?",
    "Itália", "Italy", ["Estados Unidos", "França", "Grécia"], ["United States", "France", "Greece"])

add("O croissant, apesar de associado à França, tem origem histórica em qual país?", "The croissant, though associated with France, has historical origins in which country?",
    "Áustria", "Austria", ["Bélgica", "Suíça", "Alemanha"], ["Belgium", "Switzerland", "Germany"])

add("O kimchi, prato fermentado de repolho, é um alimento tradicional de qual país?", "Kimchi, a fermented cabbage dish, is a traditional food from which country?",
    "Coreia do Sul", "South Korea", ["Japão", "China", "Vietnã"], ["Japan", "China", "Vietnam"])

add("O hummus, pasta de grão-de-bico, é tradicional da culinária de qual região?", "Hummus, a chickpea paste, is traditional to the cuisine of which region?",
    "Oriente Médio", "Middle East", ["Sudeste Asiático", "América Central", "África Austral"], ["Southeast Asia", "Central America", "Southern Africa"])

add("Na mitologia grega, quem é o deus do trovão e rei dos deuses no Monte Olimpo?", "In Greek mythology, who is the god of thunder and king of the gods on Mount Olympus?",
    "Zeus", "Zeus", ["Poseidon", "Hades", "Apolo"], ["Poseidon", "Hades", "Apollo"])

add("Na mitologia nórdica, quem é o deus do trovão associado ao martelo Mjölnir?", "In Norse mythology, who is the god of thunder associated with the hammer Mjölnir?",
    "Thor", "Thor", ["Odin", "Loki", "Balder"], ["Odin", "Loki", "Balder"])

add("Na mitologia egípcia, qual deus tem cabeça de chacal e é associado à mumificação?", "In Egyptian mythology, which god has a jackal head and is associated with mummification?",
    "Anúbis", "Anubis", ["Rá", "Osíris", "Hórus"], ["Ra", "Osiris", "Horus"])

add("Qual é a língua mais falada no mundo em número total de falantes (incluindo não nativos)?", "Which is the most spoken language in the world by total number of speakers (including non-native)?",
    "Inglês", "English", ["Mandarim", "Espanhol", "Hindi"], ["Mandarin", "Spanish", "Hindi"])

add("Qual é a língua com maior número de falantes nativos no mundo?", "Which language has the most native speakers in the world?",
    "Mandarim", "Mandarin Chinese", ["Inglês", "Espanhol", "Árabe"], ["English", "Spanish", "Arabic"])

add("O português é a língua oficial de qual país africano de grande população, ex-colônia portuguesa?", "Portuguese is the official language of which populous African country, a former Portuguese colony?",
    "Angola", "Angola", ["Quênia", "Nigéria", "Gana"], ["Kenya", "Nigeria", "Ghana"])

add("Quantos países têm o português como língua oficial, incluindo Brasil e Portugal?", "How many countries have Portuguese as an official language, including Brazil and Portugal?",
    "Nove", "Nine", ["Cinco", "Doze", "Dezesseis"], ["Five", "Twelve", "Sixteen"])

add("Além do espanhol, qual outra língua é oficial na maior parte da Espanha, falada na Catalunha?", "Besides Spanish, which other language is official in part of Spain, spoken in Catalonia?",
    "Catalão", "Catalan", ["Basco", "Galego", "Occitano"], ["Basque", "Galician", "Occitan"])

add("Qual país tem quatro línguas oficiais: alemão, francês, italiano e romanche?", "Which country has four official languages: German, French, Italian and Romansh?",
    "Suíça", "Switzerland", ["Bélgica", "Áustria", "Luxemburgo"], ["Belgium", "Austria", "Luxembourg"])

add("Qual esporte é considerado o mais popular do mundo em número de torcedores?", "Which sport is considered the most popular in the world by number of fans?",
    "Futebol", "Football (soccer)", ["Basquete", "Críquete", "Tênis"], ["Basketball", "Cricket", "Tennis"])

add("Qual país sediou a primeira Copa do Mundo de futebol, em 1930?", "Which country hosted the first football World Cup, in 1930?",
    "Uruguai", "Uruguay", ["Brasil", "Itália", "França"], ["Brazil", "Italy", "France"])

add("Qual seleção de futebol é a que mais venceu Copas do Mundo?", "Which national football team has won the most World Cups?",
    "Brasil", "Brazil", ["Alemanha", "Itália", "Argentina"], ["Germany", "Italy", "Argentina"])

add("Em qual país nasceu o críquete, esporte muito popular na Índia e Austrália?", "In which country did cricket originate, a sport very popular in India and Australia?",
    "Inglaterra", "England", ["Índia", "Austrália", "África do Sul"], ["India", "Australia", "South Africa"])

add("Qual cidade sediou os primeiros Jogos Olímpicos da era moderna, em 1896?", "Which city hosted the first Olympic Games of the modern era, in 1896?",
    "Atenas", "Athens", ["Paris", "Londres", "Roma"], ["Paris", "London", "Rome"])

add("De quantos em quantos anos os Jogos Olímpicos de Verão normalmente acontecem?", "How many years apart do the Summer Olympic Games normally take place?",
    "Quatro anos", "Four years", ["Dois anos", "Cinco anos", "Três anos"], ["Two years", "Five years", "Three years"])

add("Qual país sediou a Copa do Mundo de futebol de 2014?", "Which country hosted the 2014 football World Cup?",
    "Brasil", "Brazil", ["África do Sul", "Rússia", "Catar"], ["South Africa", "Russia", "Qatar"])

# --- Batch 6: religioes, invencoes e cinema ---
add("Qual é a religião com o maior número de seguidores no mundo?", "Which religion has the largest number of followers in the world?",
    "Cristianismo", "Christianity", ["Islamismo", "Hinduísmo", "Budismo"], ["Islam", "Hinduism", "Buddhism"])

add("Qual cidade é considerada sagrada pelas três grandes religiões monoteístas (judaísmo, cristianismo e islamismo)?", "Which city is considered holy by the three major monotheistic religions (Judaism, Christianity and Islam)?",
    "Jerusalém", "Jerusalem", ["Meca", "Roma", "Belém"], ["Mecca", "Rome", "Bethlehem"])

add("Qual é a cidade mais sagrada do islamismo, destino da peregrinação do Hajj?", "Which is the holiest city in Islam, the destination of the Hajj pilgrimage?",
    "Meca", "Mecca", ["Medina", "Jerusalém", "Bagdá"], ["Medina", "Jerusalem", "Baghdad"])

add("Qual religião teve origem na Índia e é seguida pelo Dalai Lama?", "Which religion originated in India and is followed by the Dalai Lama?",
    "Budismo", "Buddhism", ["Hinduísmo", "Jainismo", "Sikhismo"], ["Hinduism", "Jainism", "Sikhism"])

add("Quem é considerado o inventor do telefone?", "Who is considered the inventor of the telephone?",
    "Alexander Graham Bell", "Alexander Graham Bell", ["Thomas Edison", "Nikola Tesla", "Guglielmo Marconi"], ["Thomas Edison", "Nikola Tesla", "Guglielmo Marconi"])

add("Quem é creditado pela invenção da lâmpada elétrica comercialmente viável?", "Who is credited with inventing the commercially viable electric light bulb?",
    "Thomas Edison", "Thomas Edison", ["Nikola Tesla", "Alexander Graham Bell", "James Watt"], ["Nikola Tesla", "Alexander Graham Bell", "James Watt"])

add("Quem inventou a imprensa de tipos móveis na Europa, revolucionando a impressão de livros?", "Who invented the movable-type printing press in Europe, revolutionizing book printing?",
    "Johannes Gutenberg", "Johannes Gutenberg", ["Leonardo da Vinci", "Galileu Galilei", "Isaac Newton"], ["Leonardo da Vinci", "Galileo Galilei", "Isaac Newton"])

add("Os irmãos Wright são reconhecidos por qual grande feito, em 1903?", "The Wright brothers are recognized for which major achievement, in 1903?",
    "O primeiro voo motorizado controlado", "The first controlled powered flight", ["O primeiro carro a motor", "O primeiro submarino", "O primeiro foguete espacial"], ["The first motor car", "The first submarine", "The first space rocket"])

add("Quem foi o primeiro ser humano a pisar na Lua, em 1969?", "Who was the first human to walk on the Moon, in 1969?",
    "Neil Armstrong", "Neil Armstrong", ["Buzz Aldrin", "Yuri Gagarin", "John Glenn"], ["Buzz Aldrin", "Yuri Gagarin", "John Glenn"])

add("Quem foi o primeiro ser humano a viajar ao espaço, em 1961?", "Who was the first human to travel to space, in 1961?",
    "Yuri Gagarin", "Yuri Gagarin", ["Neil Armstrong", "Alan Shepard", "Valentina Tereshkova"], ["Neil Armstrong", "Alan Shepard", "Valentina Tereshkova"])

add("Qual estúdio de cinema é famoso por filmes de animação como 'Branca de Neve' e 'Rei Leão'?", "Which film studio is famous for animated movies like 'Snow White' and 'The Lion King'?",
    "Disney", "Disney", ["Pixar", "Warner Bros", "Universal"], ["Pixar", "Warner Bros", "Universal"])

add("Em qual país fica Hollywood, o famoso centro da indústria cinematográfica?", "In which country is Hollywood, the famous center of the film industry, located?",
    "Estados Unidos", "United States", ["Reino Unido", "Canadá", "Austrália"], ["United Kingdom", "Canada", "Australia"])

add("Bollywood, uma das maiores indústrias cinematográficas do mundo, está associada a qual país?", "Bollywood, one of the largest film industries in the world, is associated with which country?",
    "Índia", "India", ["Paquistão", "Bangladesh", "Nigéria"], ["Pakistan", "Bangladesh", "Nigeria"])

add("Qual prêmio de cinema americano é considerado o mais prestigiado do mundo?", "Which American film award is considered the most prestigious in the world?",
    "Oscar", "Academy Award (Oscar)", ["Globo de Ouro", "Emmy", "Grammy"], ["Golden Globe", "Emmy", "Grammy"])

add("Qual festival de cinema francês é um dos mais prestigiados do mundo, com a Palma de Ouro?", "Which French film festival is one of the most prestigious in the world, awarding the Palme d'Or?",
    "Festival de Cannes", "Cannes Film Festival", ["Festival de Veneza", "Festival de Berlim", "Sundance"], ["Venice Film Festival", "Berlin Film Festival", "Sundance"])

add("Qual moeda é usada oficialmente no Japão?", "Which currency is officially used in Japan?",
    "Iene", "Yen", ["Won", "Yuan", "Ringgit"], ["Won", "Yuan", "Ringgit"])

add("Qual moeda é usada oficialmente na China?", "Which currency is officially used in China?",
    "Yuan (renminbi)", "Yuan (renminbi)", ["Iene", "Won", "Dong"], ["Yen", "Won", "Dong"])

add("Qual moeda é usada oficialmente no Reino Unido?", "Which currency is officially used in the United Kingdom?",
    "Libra esterlina", "Pound sterling", ["Euro", "Dólar", "Franco"], ["Euro", "Dollar", "Franc"])

add("Qual moeda é usada oficialmente na Índia?", "Which currency is officially used in India?",
    "Rupia", "Rupee", ["Rublo", "Riyal", "Taka"], ["Ruble", "Riyal", "Taka"])

add("Qual moeda é usada oficialmente na Rússia?", "Which currency is officially used in Russia?",
    "Rublo", "Ruble", ["Hryvnia", "Lev", "Zloty"], ["Hryvnia", "Lev", "Zloty"])

add("Qual é o nome do time de futebol mais associado à cidade de Barcelona, na Espanha?", "What is the name of the football club most associated with the city of Barcelona, Spain?",
    "FC Barcelona", "FC Barcelona", ["Real Madrid", "Atlético de Madrid", "Sevilla"], ["Real Madrid", "Atlético Madrid", "Sevilla"])

add("Qual jogador de futebol brasileiro é frequentemente citado como um dos maiores de todos os tempos, campeão de três Copas do Mundo?", "Which Brazilian football player is often cited as one of the greatest of all time, three-time World Cup champion?",
    "Pelé", "Pelé", ["Ronaldinho", "Romário", "Zico"], ["Ronaldinho", "Romário", "Zico"])

# --- Batch 7: documentos historicos e direitos ---
add("Em que ano foi assinada a Magna Carta, documento inglês que limitou o poder do rei?", "In what year was the Magna Carta signed, the English document that limited the king's power?",
    "1215", "1215", ["1066", "1500", "1789"], ["1066", "1500", "1789"])

add("Em que ano foi assinada a Constituição dos Estados Unidos?", "In what year was the United States Constitution signed?",
    "1787", "1787", ["1776", "1800", "1865"], ["1776", "1800", "1865"])

add("Em que ano foi adotada a Declaração Universal dos Direitos Humanos pela ONU?", "In what year was the Universal Declaration of Human Rights adopted by the UN?",
    "1948", "1948", ["1945", "1919", "1960"], ["1945", "1919", "1960"])

add("Quem foi o líder do movimento pelos direitos civis nos Estados Unidos, autor do discurso 'Eu Tenho um Sonho'?", "Who led the civil rights movement in the United States, author of the 'I Have a Dream' speech?",
    "Martin Luther King Jr.", "Martin Luther King Jr.", ["Malcolm X", "Rosa Parks", "Barack Obama"], ["Malcolm X", "Rosa Parks", "Barack Obama"])

add("Em que ano foi assinada a Lei dos Direitos Civis (Civil Rights Act) nos Estados Unidos?", "In what year was the Civil Rights Act signed in the United States?",
    "1964", "1964", ["1950", "1970", "1945"], ["1950", "1970", "1945"])

add("Qual país foi o primeiro do mundo a garantir o direito de voto às mulheres, em 1893?", "Which country was the first in the world to grant women the right to vote, in 1893?",
    "Nova Zelândia", "New Zealand", ["Estados Unidos", "Reino Unido", "Finlândia"], ["United States", "United Kingdom", "Finland"])

add("Em que ano as mulheres conquistaram o direito ao voto nos Estados Unidos?", "In what year did women gain the right to vote in the United States?",
    "1920", "1920", ["1900", "1945", "1965"], ["1900", "1945", "1965"])

add("Em que ano as mulheres conquistaram o direito ao voto no Brasil?", "In what year did women gain the right to vote in Brazil?",
    "1932", "1932", ["1889", "1945", "1964"], ["1889", "1945", "1964"])

add("O ano de 1960 ficou conhecido como o 'Ano da África' por qual motivo?", "The year 1960 became known as the 'Year of Africa' for what reason?",
    "Dezessete países africanos conquistaram independência", "Seventeen African countries gained independence", ["A União Africana foi fundada", "Terminou o apartheid", "Começou a Guerra Fria"], ["The African Union was founded", "Apartheid ended", "The Cold War began"])

add("Como ficou conhecido o período de tensão entre Estados Unidos e União Soviética após a Segunda Guerra Mundial?", "What is the period of tension between the United States and the Soviet Union after World War II known as?",
    "Guerra Fria", "Cold War", ["Guerra dos Cem Anos", "Belle Époque", "Détente"], ["Hundred Years' War", "Belle Époque", "Détente"])

add("Qual muralha simbolizava a divisão entre Alemanha Ocidental e Oriental durante a Guerra Fria?", "Which wall symbolized the division between West and East Germany during the Cold War?",
    "Muro de Berlim", "Berlin Wall", ["Muralha da China", "Muro de Adriano", "Linha Maginot"], ["Great Wall of China", "Hadrian's Wall", "Maginot Line"])

add("Qual organização humanitária, fundada na Suíça, é conhecida por seu símbolo de uma cruz vermelha?", "Which humanitarian organization, founded in Switzerland, is known for its red cross symbol?",
    "Cruz Vermelha", "Red Cross", ["Médicos Sem Fronteiras", "UNICEF", "Anistia Internacional"], ["Doctors Without Borders", "UNICEF", "Amnesty International"])

add("Quem fundou o movimento que resultou na criação da Cruz Vermelha, após testemunhar a Batalha de Solferino?", "Who founded the movement that led to the creation of the Red Cross, after witnessing the Battle of Solferino?",
    "Henry Dunant", "Henry Dunant", ["Alfred Nobel", "Jean-Jacques Rousseau", "Woodrow Wilson"], ["Alfred Nobel", "Jean-Jacques Rousseau", "Woodrow Wilson"])

add("Qual organização da ONU é focada especificamente na saúde global?", "Which UN organization is specifically focused on global health?",
    "Organização Mundial da Saúde (OMS)", "World Health Organization (WHO)", ["UNICEF", "UNESCO", "PNUD"], ["UNICEF", "UNESCO", "UNDP"])

add("Qual organização da ONU é focada na proteção e no bem-estar das crianças?", "Which UN organization is focused on protecting and supporting children's welfare?",
    "UNICEF", "UNICEF", ["OMS", "UNESCO", "ACNUR"], ["WHO", "UNESCO", "UNHCR"])

add("Qual agência da ONU cuida de refugiados ao redor do mundo?", "Which UN agency deals with refugees around the world?",
    "ACNUR", "UNHCR", ["UNICEF", "UNESCO", "PNUMA"], ["UNICEF", "UNESCO", "UNEP"])

add("Qual é o nome do bloco de países membros da antiga União Soviética que mantêm cooperação, como a CEI?", "What is the name of the bloc of former Soviet Union member countries that maintain cooperation, such as the CIS?",
    "Comunidade dos Estados Independentes", "Commonwealth of Independent States", ["União Eurasiática", "Pacto de Varsóvia", "OTAN"], ["Eurasian Union", "Warsaw Pact", "NATO"])

add("Qual aliança militar foi formada pela União Soviética e países do Leste Europeu durante a Guerra Fria, em resposta à OTAN?", "Which military alliance was formed by the Soviet Union and Eastern European countries during the Cold War, in response to NATO?",
    "Pacto de Varsóvia", "Warsaw Pact", ["Comunidade dos Estados Independentes", "União Europeia", "Liga Árabe"], ["Commonwealth of Independent States", "European Union", "Arab League"])

add("Qual organização reúne países de língua e cultura árabe para cooperação regional?", "Which organization brings together Arabic-speaking countries for regional cooperation?",
    "Liga Árabe", "Arab League", ["União Africana", "ASEAN", "Conselho da Europa"], ["African Union", "ASEAN", "Council of Europe"])

add("Qual organização regional reúne países do Sudeste Asiático, como Indonésia, Tailândia e Vietnã?", "Which regional organization brings together Southeast Asian countries, such as Indonesia, Thailand and Vietnam?",
    "ASEAN", "ASEAN", ["União Africana", "Mercosul", "Liga Árabe"], ["African Union", "Mercosur", "Arab League"])

add("Qual organização reúne quase todos os países do continente africano para promover integração e paz?", "Which organization brings together nearly all African countries to promote integration and peace?",
    "União Africana", "African Union", ["Liga Árabe", "ASEAN", "Commonwealth"], ["Arab League", "ASEAN", "Commonwealth"])

add("O que é a Commonwealth, organização que reúne o Reino Unido e ex-colônias como Canadá, Austrália e Índia?", "What is the Commonwealth, the organization that brings together the United Kingdom and former colonies like Canada, Australia and India?",
    "Uma associação de países historicamente ligados ao Império Britânico", "An association of countries historically linked to the British Empire", ["Uma aliança militar da OTAN", "Um bloco de moeda única", "Um tribunal internacional"], ["A NATO military alliance", "A single-currency bloc", "An international court"])

# --- Batch 8: civilizacoes antigas e ciencia ---
add("Qual civilização antiga é considerada uma das primeiras a desenvolver a escrita, na região da Mesopotâmia?", "Which ancient civilization is considered one of the first to develop writing, in the Mesopotamia region?",
    "Sumérios", "Sumerians", ["Egípcios", "Fenícios", "Persas"], ["Egyptians", "Phoenicians", "Persians"])

add("Qual sistema de escrita antigo egípcio usava desenhos e símbolos?", "Which ancient Egyptian writing system used pictures and symbols?",
    "Hieróglifos", "Hieroglyphics", ["Cuneiforme", "Alfabeto fenício", "Escrita rúnica"], ["Cuneiform", "Phoenician alphabet", "Runic writing"])

add("Qual civilização antiga desenvolveu a escrita cuneiforme, na região onde hoje fica o Iraque?", "Which ancient civilization developed cuneiform writing, in the region where Iraq is today?",
    "Sumérios (Mesopotâmia)", "Sumerians (Mesopotamia)", ["Maias", "Astecas", "Fenícios"], ["Mayans", "Aztecs", "Phoenicians"])

add("Qual civilização pré-colombiana construiu Machu Picchu e dominava os Andes?", "Which pre-Columbian civilization built Machu Picchu and dominated the Andes?",
    "Incas", "Incas", ["Maias", "Astecas", "Olmecas"], ["Mayans", "Aztecs", "Olmecs"])

add("Qual civilização pré-colombiana dominava o atual território do México central quando os espanhóis chegaram?", "Which pre-Columbian civilization dominated present-day central Mexico when the Spanish arrived?",
    "Astecas", "Aztecs", ["Incas", "Maias", "Olmecas"], ["Incas", "Mayans", "Olmecs"])

add("Qual civilização antiga era conhecida por sua avançada astronomia e pelo calendário associado à data 2012?", "Which ancient civilization was known for its advanced astronomy and the calendar associated with the year 2012?",
    "Maia", "Maya", ["Asteca", "Inca", "Olmeca"], ["Aztec", "Inca", "Olmec"])

add("Qual antigo império teve como capital Roma e dominou grande parte da Europa, Norte da África e Oriente Médio?", "Which ancient empire had Rome as its capital and dominated much of Europe, North Africa and the Middle East?",
    "Império Romano", "Roman Empire", ["Império Bizantino", "Império Persa", "Império Otomano"], ["Byzantine Empire", "Persian Empire", "Ottoman Empire"])

add("Qual antigo imperador romano é associado à frase 'Vim, vi, venci' (Veni, vidi, vici)?", "Which ancient Roman leader is associated with the phrase 'I came, I saw, I conquered' (Veni, vidi, vici)?",
    "Júlio César", "Julius Caesar", ["Augusto", "Nero", "Marco Aurélio"], ["Augustus", "Nero", "Marcus Aurelius"])

add("Qual império, com capital em Constantinopla, sucedeu o Império Romano do Oriente?", "Which empire, with its capital in Constantinople, succeeded the Eastern Roman Empire?",
    "Império Bizantino", "Byzantine Empire", ["Império Otomano", "Império Persa", "Império Mongol"], ["Ottoman Empire", "Persian Empire", "Mongol Empire"])

add("Qual império, liderado por sultões, teve Istambul (antiga Constantinopla) como capital por séculos?", "Which empire, led by sultans, had Istanbul (former Constantinople) as its capital for centuries?",
    "Império Otomano", "Ottoman Empire", ["Império Bizantino", "Império Persa", "Império Árabe"], ["Byzantine Empire", "Persian Empire", "Arab Empire"])

add("Qual filósofo grego foi mestre de Alexandre, o Grande, e aluno de Platão?", "Which Greek philosopher was Alexander the Great's tutor and a student of Plato?",
    "Aristóteles", "Aristotle", ["Sócrates", "Pitágoras", "Heráclito"], ["Socrates", "Pythagoras", "Heraclitus"])

add("Qual filósofo grego foi condenado à morte em Atenas e é conhecido pelo método socrático de perguntas?", "Which Greek philosopher was sentenced to death in Athens and is known for the Socratic method of questioning?",
    "Sócrates", "Socrates", ["Platão", "Aristóteles", "Epicuro"], ["Plato", "Aristotle", "Epicurus"])

add("Quem foi o rei macedônio que criou um dos maiores impérios da Antiguidade, chegando até a Índia?", "Who was the Macedonian king who created one of the largest empires of antiquity, reaching as far as India?",
    "Alexandre, o Grande", "Alexander the Great", ["Júlio César", "Dario I", "Ciro, o Grande"], ["Julius Caesar", "Darius I", "Cyrus the Great"])

add("Qual cientista italiano defendeu o modelo heliocêntrico e entrou em conflito com a Igreja Católica?", "Which Italian scientist defended the heliocentric model and clashed with the Catholic Church?",
    "Galileu Galilei", "Galileo Galilei", ["Nicolau Copérnico", "Isaac Newton", "Johannes Kepler"], ["Nicolaus Copernicus", "Isaac Newton", "Johannes Kepler"])

add("Qual cientista polonês propôs que a Terra e os planetas giram ao redor do Sol, e não o contrário?", "Which Polish scientist proposed that the Earth and planets revolve around the Sun, rather than the opposite?",
    "Nicolau Copérnico", "Nicolaus Copernicus", ["Galileu Galilei", "Johannes Kepler", "Tycho Brahe"], ["Galileo Galilei", "Johannes Kepler", "Tycho Brahe"])

add("Qual cientista inglês formulou a teoria da gravitação universal?", "Which English scientist formulated the theory of universal gravitation?",
    "Isaac Newton", "Isaac Newton", ["Albert Einstein", "Galileu Galilei", "Charles Darwin"], ["Albert Einstein", "Galileo Galilei", "Charles Darwin"])

add("Qual naturalista britânico propôs a teoria da evolução por seleção natural?", "Which British naturalist proposed the theory of evolution by natural selection?",
    "Charles Darwin", "Charles Darwin", ["Gregor Mendel", "Louis Pasteur", "Alfred Russel Wallace (co-autor menos citado)"], ["Gregor Mendel", "Louis Pasteur", "Alfred Russel Wallace (less-cited co-author)"])

add("Qual cientista francês desenvolveu a pasteurização e contribuiu para a microbiologia?", "Which French scientist developed pasteurization and contributed to microbiology?",
    "Louis Pasteur", "Louis Pasteur", ["Marie Curie", "Antoine Lavoisier", "René Descartes"], ["Marie Curie", "Antoine Lavoisier", "René Descartes"])

add("Qual movimento cultural e artístico europeu, iniciado na Itália, marcou a transição da Idade Média para a Idade Moderna?", "Which European cultural and artistic movement, starting in Italy, marked the transition from the Middle Ages to the Modern Age?",
    "Renascimento", "Renaissance", ["Iluminismo", "Barroco", "Romantismo"], ["Enlightenment", "Baroque", "Romanticism"])

add("Qual movimento filosófico e intelectual do século XVIII valorizava a razão e influenciou revoluções como a Francesa?", "Which 18th-century philosophical and intellectual movement valued reason and influenced revolutions like the French Revolution?",
    "Iluminismo", "Enlightenment", ["Renascimento", "Romantismo", "Barroco"], ["Renaissance", "Romanticism", "Baroque"])

# --- Batch 9: figuras e culturas do mundo todo ---
add("Quem foi o líder venezuelano conhecido como 'O Libertador', que ajudou a libertar vários países sul-americanos da Espanha?", "Who was the Venezuelan leader known as 'The Liberator', who helped free several South American countries from Spain?",
    "Simón Bolívar", "Simón Bolívar", ["José de San Martín", "Bernardo O'Higgins", "Antonio José de Sucre"], ["José de San Martín", "Bernardo O'Higgins", "Antonio José de Sucre"])

add("Quem foi o general argentino que liderou a independência do Chile e do Peru, ao lado de Bolívar?", "Who was the Argentine general who led the independence of Chile and Peru, alongside Bolívar?",
    "José de San Martín", "José de San Martín", ["Simón Bolívar", "Bernardo O'Higgins", "Miguel Hidalgo"], ["Simón Bolívar", "Bernardo O'Higgins", "Miguel Hidalgo"])

add("Quem foi o padre mexicano que iniciou o movimento de independência do México em 1810, com o 'Grito de Dolores'?", "Who was the Mexican priest who started Mexico's independence movement in 1810, with the 'Cry of Dolores'?",
    "Miguel Hidalgo", "Miguel Hidalgo", ["Benito Juárez", "Emiliano Zapata", "Pancho Villa"], ["Benito Juárez", "Emiliano Zapata", "Pancho Villa"])

add("Quem foi o líder revolucionário mexicano associado à reforma agrária e à frase 'A terra é de quem a trabalha'?", "Who was the Mexican revolutionary leader associated with land reform and the phrase 'The land belongs to those who work it'?",
    "Emiliano Zapata", "Emiliano Zapata", ["Pancho Villa", "Benito Juárez", "Porfirio Díaz"], ["Pancho Villa", "Benito Juárez", "Porfirio Díaz"])

add("Quem foi o líder do movimento pela independência do Gana e primeiro presidente do país?", "Who led Ghana's independence movement and became the country's first president?",
    "Kwame Nkrumah", "Kwame Nkrumah", ["Nelson Mandela", "Julius Nyerere", "Jomo Kenyatta"], ["Nelson Mandela", "Julius Nyerere", "Jomo Kenyatta"])

add("Quem foi o primeiro presidente do Quênia após sua independência?", "Who was the first president of Kenya after its independence?",
    "Jomo Kenyatta", "Jomo Kenyatta", ["Kwame Nkrumah", "Nelson Mandela", "Idi Amin"], ["Kwame Nkrumah", "Nelson Mandela", "Idi Amin"])

add("Quem foi o líder revolucionário argentino-cubano, ícone da Revolução Cubana, conhecido pelo apelido 'Che'?", "Who was the Argentine-Cuban revolutionary leader, an icon of the Cuban Revolution, known by the nickname 'Che'?",
    "Ernesto 'Che' Guevara", "Ernesto 'Che' Guevara", ["Fidel Castro", "Raúl Castro", "Camilo Cienfuegos"], ["Fidel Castro", "Raúl Castro", "Camilo Cienfuegos"])

add("Quem foi o líder indiano que se tornou o primeiro primeiro-ministro da Índia independente?", "Who was the Indian leader who became independent India's first prime minister?",
    "Jawaharlal Nehru", "Jawaharlal Nehru", ["Mahatma Gandhi", "Muhammad Ali Jinnah", "Indira Gandhi"], ["Mahatma Gandhi", "Muhammad Ali Jinnah", "Indira Gandhi"])

add("Quem foi o fundador do Paquistão como nação separada da Índia britânica?", "Who was the founder of Pakistan as a nation separate from British India?",
    "Muhammad Ali Jinnah", "Muhammad Ali Jinnah", ["Jawaharlal Nehru", "Mahatma Gandhi", "Liaquat Ali Khan"], ["Jawaharlal Nehru", "Mahatma Gandhi", "Liaquat Ali Khan"])

add("Quem foi a rainha do Reino Unido com o reinado mais longo da história britânica, encerrado em 2022?", "Who was the Queen of the United Kingdom with the longest reign in British history, ending in 2022?",
    "Elizabeth II", "Elizabeth II", ["Vitória", "Ana", "Elizabeth I"], ["Victoria", "Anne", "Elizabeth I"])

add("Quem sucedeu a Rainha Elizabeth II no trono britânico em 2022?", "Who succeeded Queen Elizabeth II on the British throne in 2022?",
    "Rei Charles III", "King Charles III", ["Príncipe William", "Rei George VI", "Príncipe Harry"], ["Prince William", "King George VI", "Prince Harry"])

add("Qual imperatriz russa é conhecida como Catarina, a Grande, por expandir muito o território russo?", "Which Russian empress is known as Catherine the Great for greatly expanding Russian territory?",
    "Catarina II", "Catherine II", ["Ana da Rússia", "Isabel da Rússia", "Alexandra Feodorovna"], ["Anna of Russia", "Elizabeth of Russia", "Alexandra Feodorovna"])

add("Qual czar russo é conhecido como Pedro, o Grande, por modernizar a Rússia e fundar São Petersburgo?", "Which Russian tsar is known as Peter the Great for modernizing Russia and founding Saint Petersburg?",
    "Pedro I", "Peter I", ["Ivan, o Terrível", "Nicolau II", "Alexandre I"], ["Ivan the Terrible", "Nicholas II", "Alexander I"])

add("Quem foi o líder chinês que abriu a economia do país a reformas de mercado a partir de 1978?", "Who was the Chinese leader who opened the country's economy to market reforms starting in 1978?",
    "Deng Xiaoping", "Deng Xiaoping", ["Mao Zedong", "Xi Jinping", "Zhou Enlai"], ["Mao Zedong", "Xi Jinping", "Zhou Enlai"])

add("Quem foi o líder egípcio que nacionalizou o Canal de Suez em 1956?", "Who was the Egyptian leader who nationalized the Suez Canal in 1956?",
    "Gamal Abdel Nasser", "Gamal Abdel Nasser", ["Anwar Sadat", "Hosni Mubarak", "Rei Farouk"], ["Anwar Sadat", "Hosni Mubarak", "King Farouk"])

add("Qual canal artificial liga o Mar Mediterrâneo ao Mar Vermelho, importante para o comércio mundial?", "Which artificial canal connects the Mediterranean Sea to the Red Sea, important for world trade?",
    "Canal de Suez", "Suez Canal", ["Canal do Panamá", "Canal da Mancha", "Estreito de Gibraltar"], ["Panama Canal", "English Channel", "Strait of Gibraltar"])

add("Qual canal artificial liga o Oceano Atlântico ao Oceano Pacífico, na América Central?", "Which artificial canal connects the Atlantic Ocean to the Pacific Ocean, in Central America?",
    "Canal do Panamá", "Panama Canal", ["Canal de Suez", "Canal de Corinto", "Estreito de Magalhães"], ["Suez Canal", "Corinth Canal", "Strait of Magellan"])

add("Quem foi o líder que governou a Índia como primeira-ministra e foi assassinada em 1984?", "Who was the leader who governed India as prime minister and was assassinated in 1984?",
    "Indira Gandhi", "Indira Gandhi", ["Sonia Gandhi", "Mahatma Gandhi", "Pratibha Patil"], ["Sonia Gandhi", "Mahatma Gandhi", "Pratibha Patil"])

add("Quem foi a primeira-ministra britânica conhecida como a 'Dama de Ferro'?", "Who was the British prime minister known as the 'Iron Lady'?",
    "Margaret Thatcher", "Margaret Thatcher", ["Theresa May", "Liz Truss", "Angela Merkel"], ["Theresa May", "Liz Truss", "Angela Merkel"])

add("Quem foi a chanceler alemã que governou a Alemanha por 16 anos, até 2021?", "Who was the German chancellor who governed Germany for 16 years, until 2021?",
    "Angela Merkel", "Angela Merkel", ["Margaret Thatcher", "Olaf Scholz", "Ursula von der Leyen"], ["Margaret Thatcher", "Olaf Scholz", "Ursula von der Leyen"])

# --- Batch 10: cultura e geografia diversas ---
add("Qual é o oceano mais extenso do mundo?", "What is the largest ocean in the world?",
    "Oceano Pacífico", "Pacific Ocean", ["Oceano Atlântico", "Oceano Índico", "Oceano Ártico"], ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean"])

add("Qual é o continente mais populoso do mundo?", "What is the most populous continent in the world?",
    "Ásia", "Asia", ["África", "Europa", "América"], ["Africa", "Europe", "America"])

add("Qual é o menor continente do mundo em área terrestre?", "What is the smallest continent in the world by land area?",
    "Oceania", "Oceania", ["Europa", "Antártida", "América do Sul"], ["Europe", "Antarctica", "South America"])

add("Qual país ocupa a maior parte do continente sul-americano em área?", "Which country occupies the largest part of the South American continent by area?",
    "Brasil", "Brazil", ["Argentina", "Peru", "Colômbia"], ["Argentina", "Peru", "Colombia"])

add("Qual é o único país sul-americano que não faz fronteira com o Brasil?", "Which is the only South American country that does not share a border with Brazil?",
    "Chile", "Chile", ["Equador", "Uruguai", "Paraguai"], ["Ecuador", "Uruguay", "Paraguay"])

add("Qual é o único país da América do Sul cuja língua oficial é o inglês?", "Which is the only South American country whose official language is English?",
    "Guiana", "Guyana", ["Suriname", "Belize (América Central)", "Jamaica (Caribe)"], ["Suriname", "Belize (Central America)", "Jamaica (Caribbean)"])

add("Qual é a língua oficial do Suriname, país sul-americano ex-colônia holandesa?", "What is the official language of Suriname, a South American country and former Dutch colony?",
    "Holandês", "Dutch", ["Inglês", "Francês", "Espanhol"], ["English", "French", "Spanish"])

add("Qual é o único país da América do Sul cuja língua oficial é o francês?", "Which South American territory has French as an official language?",
    "Guiana Francesa", "French Guiana", ["Guiana", "Suriname", "Venezuela"], ["Guyana", "Suriname", "Venezuela"])

add("Qual estreito separa a Europa da África entre a Espanha e o Marrocos?", "Which strait separates Europe from Africa between Spain and Morocco?",
    "Estreito de Gibraltar", "Strait of Gibraltar", ["Canal da Mancha", "Estreito de Bering", "Bósforo"], ["English Channel", "Bering Strait", "Bosphorus"])

add("Qual estreito separa a Ásia da América, entre a Rússia e o Alasca?", "Which strait separates Asia from America, between Russia and Alaska?",
    "Estreito de Bering", "Bering Strait", ["Estreito de Gibraltar", "Bósforo", "Canal da Mancha"], ["Strait of Gibraltar", "Bosphorus", "English Channel"])

add("Qual estreito, na Turquia, é considerado a fronteira entre a Europa e a Ásia?", "Which strait, in Turkey, is considered the border between Europe and Asia?",
    "Bósforo", "Bosphorus", ["Estreito de Gibraltar", "Estreito de Bering", "Canal de Suez"], ["Strait of Gibraltar", "Bering Strait", "Suez Canal"])

add("Qual é a capital cultural e financeira da Turquia, embora não seja a capital política?", "What is Turkey's cultural and financial capital, although it is not the political capital?",
    "Istambul", "Istanbul", ["Ancara", "Esmirna", "Bursa"], ["Ankara", "Izmir", "Bursa"])

add("Qual país tem duas capitais reconhecidas informalmente, sendo uma delas a sede administrativa em Pretória?", "Which country informally has multiple capitals, with the administrative seat in Pretoria?",
    "África do Sul", "South Africa", ["Namíbia", "Botsuana", "Zimbábue"], ["Namibia", "Botswana", "Zimbabwe"])

add("Além de Pretória, quais são as outras duas capitais da África do Sul (legislativa e judiciária)?", "Besides Pretoria, what are South Africa's other two capitals (legislative and judicial)?",
    "Cidade do Cabo e Bloemfontein", "Cape Town and Bloemfontein", ["Joanesburgo e Durban", "Durban e Port Elizabeth", "Joanesburgo e Bloemfontein"], ["Johannesburg and Durban", "Durban and Port Elizabeth", "Johannesburg and Bloemfontein"])

add("Qual país tem a maior população muçulmana do mundo?", "Which country has the largest Muslim population in the world?",
    "Indonésia", "Indonesia", ["Arábia Saudita", "Paquistão", "Egito"], ["Saudi Arabia", "Pakistan", "Egypt"])

add("Qual país é considerado o berço do islamismo, onde nasceu o profeta Maomé?", "Which country is considered the birthplace of Islam, where the prophet Muhammad was born?",
    "Arábia Saudita", "Saudi Arabia", ["Egito", "Irã", "Iraque"], ["Egypt", "Iran", "Iraq"])

add("Qual é a bandeira que tem o formato não retangular, único entre os países do mundo?", "Which country has a non-rectangular flag, unique among the world's nations?",
    "Nepal", "Nepal", ["Butão", "Suíça", "Vaticano"], ["Bhutan", "Switzerland", "Vatican City"])

add("Qual é o único país cuja bandeira nacional é um quadrado perfeito?", "Which is the only country whose national flag is a perfect square?",
    "Suíça", "Switzerland", ["Vaticano", "Nepal", "Mônaco"], ["Vatican City", "Nepal", "Monaco"])

add("Qual cor está presente na maioria das bandeiras nacionais do mundo?", "Which color is present in the majority of the world's national flags?",
    "Vermelho", "Red", ["Verde", "Roxo", "Rosa"], ["Green", "Purple", "Pink"])

add("Qual símbolo aparece na bandeira do Canadá?", "What symbol appears on the flag of Canada?",
    "Folha de bordo (maple leaf)", "Maple leaf", ["Folha de carvalho", "Estrela", "Águia"], ["Oak leaf", "Star", "Eagle"])

add("Qual animal aparece no brasão e em símbolos oficiais do México, presente também na bandeira?", "Which animal appears on Mexico's coat of arms and official symbols, also present on the flag?",
    "Águia", "Eagle", ["Jaguar", "Serpente (sozinha, sem águia)", "Touro"], ["Jaguar", "Snake (alone, without eagle)", "Bull"])

add("Qual país tem uma folha de bordo (maple leaf) vermelha como símbolo central de sua bandeira?", "Which country has a red maple leaf as the central symbol of its flag?",
    "Canadá", "Canada", ["Estados Unidos", "Reino Unido", "Austrália"], ["United States", "United Kingdom", "Australia"])

# BATCH_MARKER

with open("../data/politica-cultura.json", "w", encoding="utf-8") as f:
    out = []
    for i, (qpt, opt_pt, ans, qen, opt_en) in enumerate(items):
        out.append({
            "id": f"pc-{i+1}",
            "category": "politica-cultura",
            "pt": {"question": qpt, "options": opt_pt},
            "en": {"question": qen, "options": opt_en},
            "answer": ans
        })
    json.dump(out, f, ensure_ascii=False, indent=2)

print("total:", len(items))
