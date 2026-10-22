from pathlib import Path
import tokenize,io,re,sys
for name in sys.argv[1:]:
    p=Path(__file__).parent/name
    tokens=[]
    for t in tokenize.generate_tokens(io.StringIO(p.read_text(encoding='utf-8')).readline):
        if t.type==tokenize.STRING and not re.match(r'(?i)[rubf]*r',t.string):
            v=re.sub(r'''(?<!\\)\\(?![\\'"]|n(?![A-Za-z]))''',lambda m:'\\\\',t.string)
            t=t._replace(string=v)
        tokens.append(t)
    p.write_text(tokenize.untokenize(tokens),encoding='utf-8')
