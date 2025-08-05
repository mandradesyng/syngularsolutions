import streamlit as st
from collections import OrderedDict

# --- INÍCIO DA BASE DE DADOS (CONTEÚDO COMPLETO) ---
checklist_content_46_2016 = """
### Prática de Gestão nº 1: Cultura de Segurança, Compromisso e Responsabilidade Gerencial
- A política de segurança, abordando os riscos específicos, foi formalmente definida e documentada? ||| **Letra da Lei (Item 1.2.1):** O Operador do Contrato deve definir e documentar a sua política de Gerenciamento da Integridade de Poços, contemplando os objetivos, as metas e o compromisso gerencial com a Segurança Operacional. §§§ **Exemplos de Evidências:** Documento formal da 'Política de Segurança Operacional', Matriz de Responsabilidades (RACI), Atas de Reunião que comprovem a aprovação pela alta gerência.
- Foi verificado se esses valores e políticas foram aprovados pela alta gerência da empresa?
- A estrutura organizacional para segurança operacional foi estabelecida e documentada, com uma clara classificação das funções e das tarefas relativas a cada cargo definido?
- Foi verificada a evidência da participação efetiva e contínua do corpo gerencial nas análises de risco e nas decisões críticas do projeto?
- O sistema de comunicação para disseminar a política, os riscos identificados e as metas de segurança a toda a Força de Trabalho foi analisado e considerado eficaz para o contexto do projeto?
- O planejamento e a provisão dos recursos necessários para a implementação do regulamento foram analisados e considerados suficientes?
- Foi comprovado que os recursos necessários (humanos, tecnológicos e financeiros) para implementar o sistema de gestão e controlar os riscos do projeto de CCS foram formalmente planejados e estão sendo providos? |||§§§ **Exemplos de Evidências:** Linhas de Orçamento (Budget), Plano de Alocação de Pessoal, Ordens de Compra e Contratos.
- A empresa garante que suas Contratadas também atendem às conformidades legais relativas ao Gerenciamento da Integridade de Poços?
---
### Prática de Gestão nº 2: Envolvimento da Força de Trabalho
- Foram estabelecidos e implementados canais formais para a participação da Força de Trabalho na elaboração, implementação e melhoria contínua dos procedimentos de segurança do poço ? |||§§§ **Exemplos de Evidências:** Atas de Reunião de Análise de Risco: Verificar se as atas de reuniões (como Análise de Risco da Tarefa , ou HAZOP da operação) listam a participação de membros da equipe da sonda.
- São promovidas atividades de conscientização e informação sobre a identificação de problemas, situações inseguras e os procedimentos para ativação de barreiras de segurança (CSB)?
---
### Prática de Gestão nº 3: Gestão de Competências
- As atribuições, responsabilidades e os requisitos mínimos de competência (formação, experiência, treinamentos) para cada função envolvida na integridade do poço foram formalmente definidos e documentados?
- Os níveis de certificação em treinamentos de controle de poço foram definidos e são exigidos para cada cargo ou função pertinente? |||§§§ **Exemplos de Evidências:** Uma pasta (física ou digital) com as cópias dos certificados de controle de poço (IWCF/IADC) de toda a equipe da sonda.
- Existem e são aplicados programas específicos para novos membros da Força de Trabalho ou para aqueles que assumem novas funções? |||§§§ **Exemplos de Evidências:** Plano de Integração (Onboarding) Documentado.
- Os mecanismos para avaliar periodicamente a competência da Força de Trabalho foram estabelecidos, implementados e documentados?
- A metodologia de acompanhamento e registro de treinamentos foi estabelecida, documentada e implementada?
- O cadastro funcional da Força de Trabalho é mantido atualizado para garantir a rastreabilidade e validade dos treinamentos?
---
### Prática de Gestão nº 4: Fatores Humanos
- Foram desenvolvidas e implementadas metodologias para avaliação dos Fatores Humanos em todas as etapas do Ciclo de Vida do Poço?
- Foi confirmada a implementação de treinamentos de Habilidades Não Técnicas (ex: comunicação em equipe, liderança, tomada de decisão sob pressão), e que o conteúdo desses treinamentos considera as lições aprendidas de incidentes?
- Foi verificado se o gerenciamento do tempo de descanso, da carga de trabalho e dos turnos da equipe é adequado para prevenir a fadiga, e se o procedimento de passagem de serviço é robusto para garantir a transferência completa de informações críticas? |||§§§ **Exemplos de Evidências:** As Escalas de Trabalho, O Procedimento de Passagem de Serviço, Passagem de Serviço Preenchidos.
- No projeto e disposição dos equipamentos de controle de poço, os fatores que possam impactar o desempenho humano foram considerados e mitigados?
---
### Prática de Gestão nº 5: Seleção, Controle e Gerenciamento de Empresas Contratadas
- Existem procedimentos estabelecidos, documentados e em uso para selecionar contratadas e avaliar periodicamente seu desempenho, considerando a qualidade dos materiais, equipamentos, serviços fornecidos e os riscos das atividades?
- Foi verificado se, ao ser constatado um desempenho insuficiente de uma contratada, um plano de ações corretivas e preventivas é formalmente elaborado e implementado, com prazos e responsáveis definidos? |||§§§ **Exemplos de Evidências:** RNC (Relatório de Não Conformidade), e-mails de "follow-up".
- Foi confirmado que um Documento de Interface (Bridging Document) é elaborado e implementado para alinhar procedimentos, normas e equipamentos entre o Operador e as Contratadas em cada etapa do ciclo da vida do poço?
---
### Prática de Gestão nº 6: Monitoramento e Melhoria Contínua do Desempenho
- Foram estabelecidos e documentados os objetivos de segurança, um conjunto de indicadores de desempenho (proativos e reativos) e as respectivas metas para avaliar a eficácia do Gerenciamento da Integridade do Poço? |||§§§ **Exemplos de Evidências:** Percentual de conclusão dos planos de inspeção e manutenção no prazo.
- Existe um procedimento implementado para monitorar e medir regularmente os indicadores, analisar periodicamente os resultados contra as metas e tratar os desvios de desempenho com planos de ação corretiva? |||§§§ **Exemplos de Evidências:** Painéis de gestão (dashboards), relatórios mensais de desempenho.
- A análise periódica das metas e indicadores é realizada, e as revisões visando à melhoria contínua são promovidas?
- O desempenho do Gerenciamento da Integridade de Poço é divulgado para a Força de Trabalho pertinente?
---
### Prática de Gestão nº 7: Auditorias
- O plano específico para esta auditoria foi formalmente elaborado e documentado, contemplando todos os itens exigidos nos itens 7.2.4 (a-g), como escopo, equipe, cronograma e parâmetros de criticidade? ||| **Letra da Lei (Item 7.2.4):** O plano de auditoria deve conter, no mínimo: a) escopo; b) procedimentos; c) equipe de auditoria; d) cronograma; e) parâmetros de criticidade; f) lista de verificação; g) instalações e poços a serem auditados.
- Foi verificado se o plano de auditoria foi elaborado considerando os insumos obrigatórios do item 7.2.4.1 (ex: resultados de auditorias anteriores, histórico de incidentes, lições aprendidas)? ||| **Letra da Lei (Item 7.2.4.1):** São insumos obrigatórios para a elaboração do plano de auditoria: a) os resultados de auditorias anteriores; b) o histórico de incidentes; c) as lições aprendidas; d) as análises de risco; e) as mudanças significativas nos procedimentos, pessoal ou equipamentos; f) os resultados do monitoramento de desempenho.
- A gerência da área auditada analisou o relatório documentou e implementou um Plano de Ação para tratar a causa-raiz de cada não conformidade, com prazos e responsáveis definidos, conforme item 7.5.1? ||| **Letra da Lei (Item 7.5.1):** "A gerência da área auditada deve analisar o relatório da auditoria e implementar um Plano de Ação para eliminar ou mitigar a causa-raiz de cada não conformidade, que deverá conter os prazos e os responsáveis pela sua implementação."
- É realizada uma análise de abrangência para avaliar se as ações corretivas das auditorias são aplicáveis a outros ativos, poços ou Contratadas?
- As lições aprendidas e as ações implementadas foram formalmente divulgadas (item 7.7.1) para a Força de Trabalho pertinente? ||| **Letra da Lei (Item 7.7.1):** "As lições aprendidas e as ações implementadas resultantes das auditorias devem ser documentadas e divulgadas para a Força de Trabalho pertinente."
---
### Prática de Gestão nº 8: Gestão da Informação e da Documentação
- Foi verificado se existe um procedimento de controle de documentos implementado que determina o fluxo de aprovação , a análise e revisão periódica , a identificação de alterações , o impedimento do uso de documentos obsoletos e a garantia de consistência e padronização das informações?
- Foi confirmado que a Força de Trabalho pertinente possui acesso adequado à documentação atualizada e que as informações e documentos de cada poço são rastreáveis ao longo de seu ciclo de vida?
- Foi analisado o documento de entrega de poço para confirmar se ele é mantido atualizado ao longo do Ciclo de Vida do Poço e se contém todas as informações mínimas obrigatórias listadas no item 8.4.1 ? ||| **Letra da Lei (Resumo do Item 8.4.1):** O Documento de Entrega de Poço deve conter, no mínimo: dados do poço, histórico operacional, estado atual, diagramas mecânicos, registros de testes, relatórios de anomalias, dados de monitoramento e informações sobre os elementos dos CSB.
---
### Prática de Gestão nº 9: Incidentes
- O procedimento de investigação define claramente como identificar e registrar incidentes, e garante que qualquer falha em um elemento do CSB será tratada como um incidente a ser registrado?
- O procedimento estabelece os critérios para a formação da equipe de investigação, assegurando o conhecimento técnico e a independência necessários para uma futura investigação?
- O procedimento assegura que uma futura investigação será iniciada em até 48 horas após o encerramento do incidente, para preservar as evidências?
- A metodologia de investigação descrita no procedimento garante que a análise irá identificar as causas-raiz, os fatores causais e a cronologia dos eventos?
- O procedimento define um modelo (template) para o relatório de investigação que já contém todos os campos obrigatórios exigidos pelo item 9.5.2 da resolução? ||| **Letra da Lei (Resumo do Item 9.5.2):** O relatório de investigação deve conter, no mínimo: sumário, descrição do incidente, cronologia, análise das causas-raiz, fatores contribuintes, recomendações, plano de ação e lições aprendidas.
- O sistema de gestão exige que, ao final de cada investigação, seja estabelecido, documentado e implementado um plano de ações corretivas e preventivas para tratar as causas-raiz?
- O procedimento inclui uma etapa obrigatória de "Análise de Abrangência" para avaliar se as liões aprendidas se aplicam a outros ativos?
- O plano de comunicação da empresa prevê a divulgação dos resultados de investigações de incidentes para a Força de Trabalho?
- O operador mantém um sistema para analisar alertas de segurança externos e demonstra como as ações pertinentes são implementadas?
---
### Prática de Gestão nº 10: Etapas do Ciclo de Vida do Poço
#### 10.1 Projeto
- O processo de projeto de poço está amparado por manuais, normas ou procedimentos internos documentados que estão alinhados aos requisitos legais e às melhores práticas da indústria?
- A adequação das profundidades de assentamento dos revestimentos foi avaliada e justificada com base em critérios de aceitação claros? ||| **Letra da Lei (Item 10.1.2.2):** O Operador do Contrato deve assegurar que as profundidades de assentamento dos revestimentos sejam adequadas, com base em critérios de aceitação, para garantir a integridade do poço. §§§ **Exemplos de Evidências:** Estudos de Geopressão, Stress Check dos Revestimentos (etc).
- O dimensionamento dos componentes do poço e equipamentos foi verificado para suportar a combinação de todos os carregamentos (pressão, temperatura, química, desgaste) ao longo do ciclo de vida do poço?
- A utilização de novas tecnologias, materiais ou métodos foi precedida por uma análise de risco formal para garantir a segurança da aplicação? ||| **Letra da Lei (Item 10.1.2.4):** A utilização de novas tecnologias, materiais ou métodos... deve ser precedida de uma análise de risco para o estabelecimento de medidas de controle e mitigação para reduzir o risco a um nível ALARP.
- O projeto do poço contempla e assegura o isolamento efetivo entre Aquíferos e outras zonas com fluidos distintos? |||§§§ **Exemplos de Evidências:** Plano de cimentação detalhado.
- O projeto do poço demonstra, através de documentação e simulações, que sua arquitetura permite o controle eficaz em caso de kick ou blowout e é compatível com os requisitos de abandono permanente? ||| **Letra da Lei (Item 10.1.2.6):** O Operador do Contrato deve assegurar que a arquitetura do poço... a) permita o controle do poço em caso de influxo; b) seja compatível com os requisitos de Abandono Permanente...
- Para este poço (se classificado como crítico), foi elaborado o pré-projeto e a análise de riscos para poços de alívio? ||| **Letra da Lei (Item 10.1.2.7):** O pré-projeto de poços classificados como críticos deve contemplar a análise de risco e o plano de contingência para perfuração de poço(s) de alívio. §§§ **Exemplos de Evidências:** Relief Well Contingency Plan.
- O processo exige que o projeto e o programa do poço sejam assinados pelos responsáveis pela elaboração, verificação e aprovação?
#### 10.2 Construção
- O plano de operações exige a realização de uma reunião técnica de planejamento com todas as contratadas antes do início da construção?
- O sistema de gestão garante o monitoramento, registro e avaliação contínua dos parâmetros de integridade?
- A metodologia de construção assegura, através de técnicas e avaliações, o isolamento efetivo dos aquíferos?
- Foi designado representantes na locação para gerenciar exclusivamente as atividades relacionadas ao Gerenciamento da Integridade de Poços?
#### 10.3 Produção
- O plano de operação para a fase de produção visa identificar, documentar e gerenciar os parâmetros operacionais que possam afetar a integridade dos elementos dos CSB do poço?
- Existem procedimentos de contingência documentados e disponíveis para a equipe, definindo as ações a serem tomadas caso os limites dos parâmetros operacionais sejam atingidos?
#### 10.4 Intervenção
- O sistema de gestão exige que toda intervenção seja precedida por um programa ou procedimento formal?
- O processo assegura que o programa de intervenção seja formalmente assinado pelos responsáveis pela sua elaboração, verificação e aprovação?
#### 10.5 Abandono
- O procedimento de abandono permanente garante o isolamento de todas as formações com Potencial de Fluxo, estabelecendo o número correto de barreiras permanentes?
- O procedimento de abandono exige que os materiais usados nas barreiras permanentes atendam a todos os critérios de desempenho (impermeabilidade, durabilidade, resistência, etc.)? ||| **Letra da Lei (Item 10.5.2.7):** Os materiais devem ser: a) impermeáveis; b) não deterioráveis; c) resistentes aos fluidos; d) com propriedade mecânica adequada; e) não sofrer contração; f) aderentes aos revestimentos e formações.
- O sistema de gestão de poços possui um mecanismo de controle para o prazo máximo e não prorrogável de 3 anos para o Abandono Temporário Não Monitorado?
---
### Prática de Gestão nº 11: Elementos Críticos de Integridade de Poço
- O sistema de gestão exige a identificação formal de todos os elementos críticos de integridade?
- A filosofia de projeto e operação determina a manutenção de, no mínimo, 2 Conjuntos Solidários de Barreiras (CSB) independentes (Primário e Secundário)?
- O processo prevê que, em situações excepcionais onde não seja tecnicamente possível manter duas barreiras independentes, uma análise de risco formal deva ser realizada?
- O projeto do poço comprova a instalação de uma válvula de segurança de subsuperfície (DHSV/SSSV) como elemento de barreira em todos os Poços Surgentes?
---
### Prática de Gestão nº 12: Análise de Riscos
- A empresa possui um procedimento estabelecido, documentado e implementado para a gestão de riscos?
- A metodologia de análise de risco e o template do relatório final atendem a todos os requisitos mínimos de conteúdo definidos na resolução?
- O sistema de gestão assegura que as recomendações da análise de risco são implementadas e divulgadas?
---
### Prática de Gestão nº 13: Integridade do Poço
- A empresa possui um sistema documentado para o gerenciamento da integridade dos poços que estabelece planos para inspeção, verificação, manutenção e monitoramento que garantem que os CSB e equipamentos críticos estejam sempre funcionais?
- O sistema de gestão comprova que a capacidade de corte dos elementos do BOP é conhecida e gerenciada?
---
### Prática de Gestão nº 14: Emergências de Controle de Poço
- A empresa possui um Plano de Resposta à Emergência para Controle de Poço que é documentado, implementado e integrado aos demais planos de emergência da companhia? ||| **Letra da Lei (Itens 14.2.1, 14.2.2, 14.2.4):** O Operador deve estabelecer, documentar e implementar um Plano de Resposta a Emergências (PRE) para Controle de Poço. Este plano deve ser integrado aos demais planos de emergência da companhia e ser consistente com as Análises de Risco. §§§ **Exemplos de Evidências:** O documento "Plano de Resposta à Emergência para Controle de Poço".
- O plano de resposta descreve os recursos e a logística necessários para os piores cenários, incluindo poços de alívio e sistemas de capeamento e contenção? ||| **Letra da Lei (Itens 14.2.5, 14.2.6):** O PRE deve prever os recursos e a logística para o controle de um blowout no pior cenário. O Operador deve assegurar o acesso a estes recursos, incluindo poços de alívio e sistemas de capeamento, podendo ser por meio de contratos de afiliação com empresas especializadas. §§§ **Exemplos de Evidências:** A seção ou apêndice do PRE que trata de "Controle de Blowout". Contratos ou acordos de afiliação com cooperativas de controle de poços (ex: OSRL).
- O sistema de gestão prevê a programação e realização periódica de exercícios simulados para os cenários de controle de poço, com avaliação de desempenho e tratamento de desvios? ||| **Letra da Lei (Item 14.3):** O Operador deve programar e realizar exercícios simulados periodicamente para avaliar seu PRE. Os resultados devem ser registrados, analisados criticamente, e as recomendações e lições aprendidas devem ser documentadas, divulgadas e implementadas. §§§ **Exemplos de Evidências:** O "Cronograma Anual de Exercícios Simulados", um "Relatório de Avaliação de Desempenho de Simulado" recente, e um "Plano de Ação Corretiva" gerado a partir do simulado.
---
### Prática de Gestão nº 15: Procedimentos
- O operador possui procedimentos claros, documentados e implementados que cobrem todas as atividades críticas para o Gerenciamento da Integridade de Poços? ||| **Letra da Lei (Item 15.2.1):** O Operador do Contrato deve estabelecer, documentar e implementar procedimentos para a execução das atividades que fazem parte do Gerenciamento da Integridade de Poços, alinhados com a Análise de Riscos. §§§ **Exemplos de Evidências:** A "Biblioteca de Procedimentos Operacionais (POP)". Verificar se existe um procedimento formal para cada atividade crítica (ex: "Procedimento de Teste do BOP", "Procedimento de Operação de Cimentação", etc.).
- Existem manuais específicos para controle de poço e gestão de pressão anular, uma metodologia para definir a criticidade dos poços e um procedimento que assegure a interrupção de atividades em caso de risco? ||| **Letra da Lei (Itens 15.2.1.1 a 15.2.1.4):** A regulamentação exige a existência de documentos específicos, incluindo: Manual de Controle de Poço, Metodologia de Classificação de Criticidade de Poços, Procedimento para Gestão de Pressão Anular e um Procedimento que assegure a interrupção de atividades (Stop Work Authority). §§§ **Exemplos de Evidências:** O "Manual de Controle de Poço", o "Procedimento de Gestão de Pressão Anular (APM)", o documento "Metodologia de Classificação de Criticidade de Poços", e o procedimento de "Autoridade para Parada de Trabalho (Stop Work Authority)".
- A empresa comprova que a Força de Trabalho é treinada nos procedimentos e que a supervisão avalia o seu cumprimento em campo? ||| **Letra da Lei (Itens 15.2.2 e 15.2.3):** O Operador deve assegurar que a Força de Trabalho seja treinada nos procedimentos aplicáveis às suas funções. A supervisão deve avaliar o cumprimento dos procedimentos durante a execução das atividades. §§§ **Exemplos de Evidências:** A "Matriz de Treinamentos por Função", os "Registros de Treinamento", e relatórios de "Verificação de Conformidade em Campo" ou "Auditorias Comportamentais".
- O gerenciamento de Operações Conjuntas, envolvendo múltiplas contratadas, é coberto por procedimentos de controle específicos? ||| **Letra da Lei (Item 15.3):** O Operador do Contrato deve estabelecer procedimentos de controle para gerenciar as interfaces e os riscos durante as Operações Conjuntas. §§§ **Exemplos de Evidências:** O "Documento de Interface (Bridging Document)", o relatório da "Análise de Risco de Operações Simultâneas (SIMOPS)". Verificar se o Documento de Interface define responsabilidades e se a análise SIMOPS foi realizada para mitigar riscos de interação.
---
### Prática de Gestão nº 16: Gestão de Mudanças
- A empresa possui um procedimento formal de Gestão de Mudanças que exige a avaliação prévia de qualquer alteração (temporária ou permanente) em operações, procedimentos, projeto ou pessoal, para manter o risco em nível ALARP? ||| **Letra da Lei (Item 16.2.1):** O Operador deve estabelecer, documentar e implementar um procedimento de Gestão de Mudanças (MOC) para alterações. O procedimento deve abranger, no mínimo: a justificativa, análise técnica, análise de riscos, aprovações, documentação, comunicação e validade da mudança. §§§ **Exemplos de Evidências:** O documento "Procedimento de Gestão de Mudanças (MOC)".
- O processo de Gestão de Mudanças garante que nenhuma alteração comprometerá o controle do poço, o seu abandono futuro ou a segurança, e exige a elaboração de um plano de ação formal para sua implementação? ||| **Letra da Lei (Itens 16.2.2 e 16.3):** A Gestão de Mudanças deve assegurar que a alteração não comprometerá o controle, o abandono ou a segurança do poço. Deve ser elaborado um plano de ação para a implementação segura da mudança, contendo as tarefas, prazos e responsáveis. §§§ **Exemplos de Evidências:** Um "Formulário de Gestão de Mudança (MOC)" já preenchido e aprovado. O "Plano de Ação para Implementação da Mudança" anexado ao MOC.
---
### Prática de Gestão nº 17: Preservação Ambiental
- A empresa comprova que todas as atividades associadas ao ciclo de vida do poço (incluindo abandono temporário) estão amparadas por autorizações ambientais vigentes e que estas estão disponíveis para consulta no local da operação? ||| **Letra da Lei (Item 17.2):** O Operador do Contrato deve obter e manter válidas todas as autorizações ambientais necessárias para as atividades do poço em todas as suas etapas. As autorizações devem estar disponíveis na instalação. §§§ **Exemplos de Evidências:** Cópia da Licença de Operação (LO), Licença de Instalação (LI) ou Licença Prévia (LP) emitida pelo órgão ambiental competente (IBAMA, órgão estadual).
- Para poços terrestres, o projeto da locação foi desenvolvido visando à minimização dos riscos e impactos ambientais, e existem planos de inspeção e manutenção da locação para todas as etapas do ciclo de vida? ||| **Letra da Lei (Item 17.3):** Para poços terrestres, o projeto da locação deve visar à minimização dos riscos e impactos ao meio ambiente e à saúde humana. O Operador deve implementar planos de inspeção e manutenção da locação durante todo o ciclo de vida. §§§ **Exemplos de Evidências:** O "Projeto Executivo da Locação" ou "Memorial Descritivo da Instalação". O "Plano de Inspeção e Manutenção da Locação".
- A empresa demonstra possuir um sistema para a gestão ambientalmente adequada de materiais, produtos e resíduos, garantindo o registro e a rastreabilidade da destinação final? ||| **Letra da Lei (Item 17.4):** O Operador do Contrato deve implementar sistema para a gestão ambientalmente adequada dos materiais, produtos e resíduos, assegurando o registro e a rastreabilidade de sua destinação final. §§§ **Exemplos de Evidências:** O "Plano de Gerenciamento de Resíduos Sólidos (PGRS)" do projeto. Os "Manifestos de Transporte de Resíduos (MTR)". Os "Certificados de Destinação Final" emitidos por empresas tratadoras licenciadas.
"""

checklist_content_699_2017 = "### Checklist em Desenvolvimento\n- O checklist detalhado para a Resolução ANP nº 699/2017 ainda não foi inserido."
placeholder_content = "### Conteúdo em Desenvolvimento\n- O material para este documento ainda não foi adicionado à aplicação."

conteudo_perfuração_ccs = {
    "Normativas": {
        "Resolução ANP nº 46/2016 (SGIP)": {"link": "https://atosoficiais.com.br/anp/resolucao-n-46-2016",
                                            "checklist_content": checklist_content_46_2016.strip().split('\n')},
        "Resolução ANP nº 699/2017": {
            "link": "https://www.gov.br/anp/pt-br/assuntos/resolucoes-anp-dsp/resolucoes-anp/resolucao-anp-no-699-2017",
            "checklist_content": checklist_content_699_2017.strip().split('\n')}
    },
    "Regras Transnacionais": {
        "Exemplo de Regra Internacional": {"link": "", "checklist_content": placeholder_content.strip().split('\n')}}
}

dados_app_completo = {
    "CCS": {
        "Perfuração de Poço Estratigráfico": conteudo_perfuração_ccs,
        "Perfuração de Poço Injetor": conteudo_perfuração_ccs,
        "Perfuração de Poço de Monitoramento": conteudo_perfuração_ccs,
        "Armazenamento Geológico": {"Normativas": {}, "Regras Transnacionais": {}},
        "Prospecção de Áreas para Estocagem": {"Normativas": {}, "Regras Transnacionais": {}},
        "Monitoramento e Gestão do Reservatório": {"Normativas": {}, "Regras Transnacionais": {}},
        "Descomissionamento": {"Normativas": {}, "Regras Transnacionais": {}}
    },
    "O&G": {"Exploração": {"Normativas": {}, "Regras Transnacionais": {}},
            "Produção": {"Normativas": {}, "Regras Transnacionais": {}}},
    "Mineração": {"Pesquisa Mineral": {"Normativas": {}, "Regras Transnacionais": {}},
                  "Lavra": {"Normativas": {}, "Regras Transnacionais": {}}}
}


# --- FIM DA BASE DE DADOS ---


def parse_checklist_to_practices(checklist_lines):
    parsed_data = OrderedDict()
    current_practice = None
    for line in checklist_lines:
        if line.startswith('### Prática de Gestão'):
            current_practice = line.replace('### ', '').strip()
            parsed_data[current_practice] = []
        elif line.startswith('-') and current_practice:
            parsed_data[current_practice].append(line)
        elif current_practice and not line.startswith('-'):
            parsed_data[current_practice].append(line)
    return parsed_data


# ==============================================================================
# FUNÇÃO PARA DESENHAR A PÁGINA INICIAL
# ==============================================================================
def pagina_inicial():
    try:
        st.image("logo.png", width=250)
    except:
        st.warning("Arquivo logo.png não encontrado. Por favor, adicione o logo na mesma pasta do script.")

    st.header("Ferramenta de Conformidade e Consulta", divider='rainbow')
    st.caption("Desenvolvido por Micaellen Andrade • Syngular Solutions Web Application 🚀")
    st.markdown("---")
    st.subheader("Por favor, selecione uma área de atuação para começar:")

    col1, col2, col3 = st.columns(3, gap="large")

    with col1:
        with st.container(border=True):
            st.markdown("### 🌎♻️ CCS")
            st.write(
                "Checklists e normativas relacionadas a projetos de Captura, Utilização e Armazenamento de Carbono.")
            if st.button("Acessar CCS", use_container_width=True, type="primary"):
                st.session_state.area_selecionada = "CCS"
                st.session_state.pagina_ativa = "checklist"
                st.rerun()

    with col2:
        with st.container(border=True):
            st.markdown("### 🛢️ O&G")
            st.write(
                "Regulamentações e melhores práticas para a indústria de Óleo e Gás (conteúdo em desenvolvimento).")
            if st.button("Acessar O&G", use_container_width=True):
                st.session_state.area_selecionada = "O&G"
                st.session_state.pagina_ativa = "checklist"
                st.rerun()

    with col3:
        with st.container(border=True):
            st.markdown("### ⛏️ Mineração")
            st.write("Normas e guias de conformidade para o setor de mineração (conteúdo em desenvolvimento).")
            if st.button("Acessar Mineração", use_container_width=True):
                st.session_state.area_selecionada = "Mineração"
                st.session_state.pagina_ativa = "checklist"
                st.rerun()


# ==============================================================================
# FUNÇÃO PARA DESENHAR A PÁGINA DE CHECKLIST
# ==============================================================================
def pagina_checklist():
    # --- BARRA LATERAL (SIDEBAR) ---
    try:
        st.sidebar.image("logo.png", use_container_width=True)
    except:
        st.sidebar.warning("Logo não encontrado.")

    area_ativa = st.session_state.area_selecionada
    st.sidebar.header(f"Área Ativa: {area_ativa}")

    if st.sidebar.button("⬅️ Voltar para a Seleção de Áreas"):
        st.session_state.pagina_ativa = "inicial"
        st.rerun()

    st.sidebar.markdown("---")

    dados_da_area = dados_app_completo[area_ativa]
    temas_ordenados = sorted(dados_da_area.keys())

    tema_selecionado = st.sidebar.selectbox("1. Selecione o Tema", temas_ordenados)
    categorias_disponiveis = list(dados_da_area[tema_selecionado].keys())
    categoria_selecionada = st.sidebar.selectbox("2. Selecione a Categoria", categorias_disponiveis)

    st.sidebar.markdown("---")
    st.sidebar.markdown("Desenvolvido por Micaellen Andrade • Syngular Solutions Web Application 🚀")

    # --- CONTEÚDO PRINCIPAL ---
    st.title(f"{tema_selecionado}")
    subtitle_mapping = {
        "Normativas": "Normativas Brasileiras / Agência Nacional do Petróleo",
        "Regras Transnacionais": "Padrões e Melhores Práticas Internacionais"
    }
    st.caption(subtitle_mapping.get(categoria_selecionada, categoria_selecionada))
    st.markdown("---")

    documentos = dados_da_area[tema_selecionado][categoria_selecionada]

    if not documentos:
        st.info("Ainda não há documentos cadastrados para esta combinação de Tema e Categoria.")
    else:
        for documento, dados in documentos.items():
            st.subheader(documento)
            with st.expander("Visualizar Checklist e Opções"):
                if dados.get("link"):
                    st.link_button("Acessar Documento Oficial ↗️", dados["link"])
                    st.markdown("---")

                linhas_checklist = dados["checklist_content"]
                parsed_checklist = parse_checklist_to_practices(linhas_checklist)

                all_task_keys_for_document = []
                for practice, questions in parsed_checklist.items():
                    for idx, question in enumerate(questions):
                        if question.startswith('-'):
                            all_task_keys_for_document.append(f"cb_{documento}_{practice}_{idx}")

                for practice, questions in parsed_checklist.items():
                    with st.expander(practice):
                        for idx, linha in enumerate(questions):
                            linha = linha.strip()
                            if not linha: continue
                            if linha.startswith('####') or linha == '---':
                                st.markdown(linha)
                                continue
                            if linha.startswith('-'):
                                task_key = f"cb_{documento}_{practice}_{idx}"
                                main_parts = linha[1:].split('§§§')
                                question_and_legal = main_parts[0]
                                example_text = main_parts[1].strip() if len(main_parts) > 1 else None
                                sub_parts = question_and_legal.split('|||')
                                pergunta = sub_parts[0].strip()
                                legal_text = sub_parts[1].strip() if len(sub_parts) > 1 else None

                                col1, col2, col3, col4 = st.columns([0.08, 0.76, 0.08, 0.08], gap="small")
                                with col1:
                                    st.checkbox(label="", key=task_key, label_visibility="collapsed")
                                with col2:
                                    st.markdown(pergunta)
                                with col3:
                                    if legal_text:
                                        with st.popover("ℹ️"): st.info(legal_text)
                                with col4:
                                    if example_text:
                                        with st.popover("📄"): st.success(example_text)

                st.markdown("---")
                num_total = len(all_task_keys_for_document)
                num_checked = sum(1 for key in all_task_keys_for_document if st.session_state.get(key, False))
                if num_total > 0:
                    progresso = num_checked / num_total
                    st.markdown(f"**Progresso Geral do Documento: {num_checked} de {num_total} itens concluídos**")
                    st.progress(progresso)
                else:
                    st.markdown("Nenhum item de checklist encontrado no formato esperado.")
            st.markdown("---")


# ==============================================================================
# "ROTEADOR" PRINCIPAL - Decide qual página mostrar
# ==============================================================================
st.set_page_config(page_title="Ferramenta de Conformidade", layout="wide")

if 'pagina_ativa' not in st.session_state:
    st.session_state.pagina_ativa = 'inicial'
if 'area_selecionada' not in st.session_state:
    st.session_state.area_selecionada = None

if st.session_state.pagina_ativa == 'inicial':
    pagina_inicial()
else:
    pagina_checklist()