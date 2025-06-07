# História dos Design Patterns

Minha intenção aqui não é fazer uma revisão bibliográfica ou pesquisa histórica sobre a origem dos Design Patterns, mas considero importante entender por que surgiram e como foram criados. Isso me ajuda a compreender melhor o contexto de sua criação e como podem ser aplicados no desenvolvimento de software.

Vamos começar respondendo uma pergunta simples: *"Quem criou ou inventou os Design Patterns?"*

Essa é uma boa pergunta, mas a resposta não é tão simples (acho que se você perguntasse quem inventou o parafuso, a resposta seria igualmente complexa :-)).

Os padrões de projeto não são conceitos obscuros ou sofisticados, assim como os parafusos. Padrões são soluções típicas para problemas de desenvolvimento de software. Provavelmente, as pessoas começaram a criar suas próprias soluções para problemas comuns desde o início do desenvolvimento de software. O que aconteceu foi que essas soluções, frequentemente, eram iguais ou muito semelhantes e, naturalmente, as pessoas começaram a discuti-las. Isso ocorre em qualquer área do conhecimento, não apenas na Engenharia de Software.

Como em toda área de conhecimento, existem pessoas dedicadas ao estudo e pesquisa do assunto, seja no meio acadêmico ou na prática profissional. Esses profissionais começaram a perceber que existiam soluções comuns para problemas recorrentes e iniciaram o processo de documentação, reconhecendo que essas soluções poderiam ser padronizadas.

O conceito de Design Patterns foi primeiramente descrito por [Christopher Alexander](https://pt.wikipedia.org/wiki/Christopher_Alexander), arquiteto, matemático e urbanista (isso é uma das coisas que mais aprecio na Tecnologia da Informação: ela é multidisciplinar e você encontra pessoas de diversas áreas trabalhando com ela). Alexander publicou o livro [**"Uma Linguagem de Padrões"**](https://www.amazon.com.br/Uma-Linguagem-Padr%C3%B5es-Christopher-Alexander/dp/8565837173), que descreve uma "linguagem" para projetos de ambiente urbano. Seu objetivo era padronizar soluções para problemas comuns de urbanismo, como a altura ideal de uma janela em relação ao chão ou o tamanho adequado de uma área verde, facilitando a implementação de soluções para esses desafios.

Em sua obra, Alexander descreve que um "padrão" deve ter as seguintes características:

- **Encapsulamento**: um padrão encapsula um problema ou solução bem definida. Deve ser independente, específico e formulado de maneira clara sobre onde se aplica.
- **Generalidade**: todo padrão deve permitir a construção de outras realizações a partir dele.
- **Equilíbrio**: quando um padrão é utilizado, o equilíbrio fornece a justificativa para cada passo do projeto, considerando todas as restrições envolvidas. Uma análise racional envolvendo abstração de dados empíricos, observação da aplicação de padrões em artefatos tradicionais, exemplos convincentes e análise de soluções inadequadas pode ser a forma de encontrar esse equilíbrio.
- **Abstração**: os padrões representam abstrações da experiência empírica ou do conhecimento cotidiano.
- **Abertura**: um padrão deve permitir sua extensão para níveis mais detalhados.
- **Combinatoriedade**: os padrões relacionam-se hierarquicamente. Padrões de alto nível podem ser compostos ou relacionados com padrões que abordam problemas de nível mais baixo.

Essa forma de pensar e abordar problemas comuns foi trazida para a Engenharia de Software por [Erich Gamma](https://pt.wikipedia.org/wiki/Erich_Gamma), [Richard Helm](https://pt.wikipedia.org/wiki/Richard_Helm), [Ralph Johnson](https://pt.wikipedia.org/wiki/Ralph_Johnson) e [John Vlissides](https://pt.wikipedia.org/wiki/John_Vlissides), que publicaram o livro [**"Padrões de Projeto – Soluções Reutilizáveis de Software Orientado a Objetos"**](https://www.amazon.com.br/Padr%C3%B5es-Projetos-Solu%C3%A7%C3%B5es-Reutiliz%C3%A1veis-Orientados/dp/8573076100) em 1994. Este livro é considerado um marco na história dos Design Patterns e um dos mais influentes na Engenharia de Software. Ele descreve 23 padrões de projeto que são soluções típicas para problemas comuns do desenvolvimento de software orientado a objetos. Devido ao título extenso, o livro é mais conhecido como **"Gang of Four"**, **"GoF"** ou, em português, **"O livro da gang dos quatro"**.

Desde então, outros padrões foram descobertos e documentados, e essa abordagem expandiu-se para outras áreas do desenvolvimento de software, como padrões de arquitetura, padrões de integração, padrões de teste, entre outros.