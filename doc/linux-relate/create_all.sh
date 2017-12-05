#!/bin/bash

main=main.tex
rm -f $main
cat main_template >> $main
cat <<EOF >> $main
\begin{document}
\frontmatter
\maketitle
\tableofcontents
\mainmatter
EOF
for i in `ls *tex |grep -v main`
do
    echo "\include{${i/.tex}}" >> $main
done
cat <<EOF >> $main
\end{document}
EOF
