# Projeto Quarta-Feira
Projeto de redes distribuídas e computação em nuvem 

Projeto Prático
Prof. Me. Michel Junio Ferreira Rosa
Arquitetura de Sistemas Distribuídos
Background P2P Híbrida
Introdução às Redes P2P
As redes peer-to-peer (P2P) são um tipo de arquitetura de rede distribuída onde cada nó (ou peer) na rede funciona tanto como cliente quanto como servidor, permitindo compartilhamento direto de recursos e informações entre os nós. Ao contrário das arquiteturas tradicionais de cliente-servidor, onde um servidor centralizado fornece recursos para clientes, nas redes P2P, cada nó pode oferecer e solicitar recursos de outros nós, criando um sistema descentralizado e colaborativo.

Tipos de Redes P2P
Existem principalmente três tipos de redes P2P:

Redes P2P Puras: Todos os nós na rede são iguais e não há um nó centralizado. Exemplos incluem Gnutella e Freenet.

Redes P2P Estruturadas: Utilizam uma tabela de hash distribuída (DHT) para organizar e procurar dados de forma eficiente. Exemplos incluem Chord e Kademlia.

Redes P2P Híbridas: Combinação de elementos das arquiteturas P2P puras e centralizadas, onde existem nós super-peers que assumem funções especiais para facilitar a comunicação e a gestão da rede.

Redes P2P Híbridas
As redes P2P híbridas surgiram para combinar os benefícios das arquiteturas P2P puras e centralizadas, mitigando algumas das limitações de cada uma. Numa rede P2P híbrida, há uma hierarquia de nós, onde certos nós (super-peers ou supernós) têm capacidades especiais ou responsabilidades adicionais, enquanto os nós regulares continuam a funcionar como em uma rede P2P pura.

Características das Redes P2P Híbridas
Super-Peers: Alguns nós são designados como super-peers devido à sua capacidade superior de processamento, armazenamento, ou conexão à rede. Estes super-peers funcionam como hubs ou mini-servidores, facilitando a comunicação e o roteamento de dados.

Eficiência de Busca: Super-peers mantêm índices de recursos disponíveis na rede, permitindo buscas mais rápidas e eficientes, evitando a necessidade de broadcast massivo de solicitações.

Escalabilidade: Redes P2P híbridas podem escalar melhor do que redes puramente centralizadas, pois a carga é distribuída entre vários super-peers, evitando pontos únicos de falha.

Robustez e Resiliência: Embora existam nós centrais (super-peers), a rede não depende de um único ponto de controle, aumentando a robustez e a resiliência contra falhas ou ataques.

Proposta de Projeto de Rede Peer-to-Peer (P2P) de Arquitetura Híbrida
Objetivo do Projeto:
Desenvolver uma rede Peer-to-Peer (P2P) em Python, focada na transferência eficiente de arquivos de diversos tipos (texto, CSV, vídeo, imagem, XLSX, etc.). O projeto utilizará nós de borda para centralizar a descoberta, o roteamento de arquivos e a manutenção das listas de arquivos e nós ativos, garantindo a eficiência e a integridade das transferências.
A arquitetura a ser proposta deve considerar os conceitos de uma rede P2P Híbrida, confome arquitetura abaixo.

Arquitetura de Rede P2P Híbrida

1. Arquitetura da Rede:
Nós Regulares: Participantes que armazenam e compartilham arquivos. Cada nó mantém uma lista dos seus arquivos, contendo o nome do arquivo e o valor de checksum para verificação de integridade.
Nós de Borda: Servidores especiais responsáveis por gerenciar informações sobre a localização dos arquivos e dos nós, facilitando a descoberta e transferência de arquivos, além de manter atualizadas as listas de nós ativos e seus arquivos.
2. Funcionalidades Principais:
Descoberta e Transferência de Arquivos: Nós de borda coordenam a localização de arquivos solicitados e direcionam as solicitações para os nós que possuem os arquivos.
Balanceamento de Carga: Distribuição equilibrada de solicitações para evitar sobrecarga em qualquer nó específico.
Manutenção de Listas Atualizadas: Nós de borda solicitam periodicamente aos nós regulares suas listas de arquivos para manter suas informações precisas e atualizadas. Se um nó não responder, ele é removido da lista de nós disponíveis.
3. Implementação:
Linguagem de Programação: Python, etc.
Comunicação via Sockets: Utilizada para a comunicação entre nós para transferência de arquivos e troca de mensagens de controle.
Programação Concorrente:
1 - Uso de threads ou processos para gerenciar múltiplas solicitações e transferências simultaneamente.
2 - Uso de threads ou processos para gerencia a lista de [Nós/Arquivos].
4. Transferência de Arquivos:
Tipos de Arquivos: Suporte a vários formatos de arquivos massivos, incluindo documentos de texto, planilhas, imagens, vídeos e arquivos CSV.
Verificação de Integridade: Cada arquivo transferido terá seu checksum calculado e verificado após o recebimento para assegurar que o conteúdo transferido não foi corrompido ou alterado.
5. Manutenção e Atualização de Listas:
Solicitação Periódica de Atualizações: Os nós de borda periodicamente se conectam a cada nó regular para solicitar suas listas de arquivos. Esta atualização é feita através de um processo que verifica a disponibilidade dos nós.
Remoção de Nós Inativos: Se um nó regular não responder às solicitações de atualização dentro de um tempo especificado, ele será considerado inativo e removido da lista de clientes disponíveis.
6. Entregáveis:
Código Fonte: Código completo do projeto em Python, incluindo todos os módulos para a execução da rede P2P.
Registros de Execução: Documentação das sessões de teste com no mínimo 4 nós, demonstrando a eficácia da descoberta de arquivos, transferência, e atualização das listas.
Evidências de Funcionamento: Screenshots, logs de execução e outras evidências que comprovem o funcionamento do sistema conforme o design proposto.
Grupo: A proposta deve ser desenvolvida por no máximo 4 (quatro) discentes.
Deadline: 20/06/2024 - Apresentar a solução funcionando no Laboratório.
7. Testes e Validação:
Ambiente de Teste: Testes em um ambiente simulado com ao menos 2 nós para validar as funcionalidades, incluindo a eficiência do sistema de balanceamento de carga, integridade dos dados após transferências, e a precisão na manutenção das listas de arquivos.
