---
width: 1920
height: 1080
minScale: 1.4
enableSearch: true
enableChalkboard: false
customTheme : "beige"
transition: "convex"
title: JupyterLab
---

# JupyterLab

2025-12-13 張

---

## 📱 JupyterLab

Webベースの対話型実行環境

* **Markdown Cell**
  * 説明文や数式を書く
* **Code Cell**
  * コードを書いてそのまま実行
  * 出力はCode Cellの下に表示
  
--

### jupyterLabシステム構成

* **Client**: セル編集・コード実行・可視化表示
* **Server**: NotebookファイルとKernelの管理
* **Kernel**: コードの実行

![](https://docs.jupyter.org/en/latest/_images/notebook_components.png)

--

### Kernel

```text
jupyter kernelspec list
```

* R: [IRkernel](https://github.com/IRkernel/IRkernel)
* Julia: [IJulia.jl](https://github.com/JuliaLang/IJulia.jl)
* C#: [interactive](https://github.com/dotnet/interactive)
* JavaScript: [deno](https://docs.deno.com/runtime/reference/cli/jupyter/)
* Rust: [evcxr](https://github.com/evcxr/evcxr)
* C++: [xeus-cling](https://github.com/jupyter-xeus/xeus-cling)
* Octave: [octave_kernel](https://github.com/Calysto/octave_kernel)

---

## Magic Commands

* **Line Magic**: `%ls`, `%time`, `%timeit`, ...
* **Cell Magic**: `%%time`, `%%writefile`, `%%prun`, ...

--

### Line Magic

```python
from IPython.core.magic import register_line_magic


@register_line_magic
def hello(line):
    for i in range(5):
        print("Hello,", line)
```

--

### Cell Magic

```python
from IPython.core.magic import register_cell_magic


@register_cell_magic
def demo(line, cell):
    print("line arguments  :", line)
    print("cell content:\n", cell)
```

--

### Magic Command 例

* `%%cffi`: C言語関数を実行
* `%%dot`: Graphvizでグラフ出力
* `%%sympy`: 数式計算
* `%%regexfind`: 正規表現で検索
* `%%ast_mermaid`: コードの抽象構文木表示

---

### Outputs

* PNG & SVG Plot: `matplotlib`
* Table: `polars, itable`
* JavaScript Plot: `altair, bokeh, plotly`
* 3D: `pyvista`
* Network Graph: `ipysigma`
 
--

## GUI

--

### ipywidgets

```python
from ipywidgets import interact

def foo(a, b, c, d, e, f):
    return f'Arguments: {a, b, c, d, e, f}'

interact(
    foo,
    a=True,
    b=10,
    c=(20, 30, 2),
    d='text',
    e=['apples', 'oranges'],
    f=dict([('first', 10), ('second', 20)])
)
```

--

### panel

```python
import panel as pn


def foo(a, b, c, d, e, f):
    return f'Arguments: {a, b, c, d, e, f}'

pn.interact(
    foo,
    a=True,
    b=10,
    c=(-10, 10, 0.1, 5.4),
    d='text',
    e=['apples', 'oranges'],
    f=dict([('first', 10), ('second', 20)])
)
```

---

## ipynbフォーマット

* json形式
* nbformatライブラリで処理

--

## ChatGPTセッションからNotebookの自動生成


> Here is an example of the JSON data from a ChatGPT chat session:
> ...
> * Please write a Python script that saves all AI outputs into an `.ipynb` notebook.
> * Code sections in the answers should be converted into **code cells** in the notebook.
> * All other sections should be converted into **markdown cells**.

--

## DeepSeek APIによる自動翻訳

> You are a helpful Chinese to Japanese translator.
> * Translate the text from Chinese into Japanese. 
> * Please use 丁寧語. 
> * Keep the original text format. Keep the line starts with **$$$** unchanged.
> * don't change the source code, only translate the comments in it.
> * Do not add any unrelated words or comments to the translation.

---

## Jupyter Boook

Notebookからドキュメントサイト作成

```text
pip install jupyter-book==1.0.4.post1
jupyter-book create book
jupyter-book build book
```

--

### _toc.yml

```text
format: jb-book
root: intro
chapters:
  - file: notebooks
  - file: myst-guide
    sections:
      - file: myst-directives
      - file: myst-syntax
```

--

### _config.yml

```text
# 書籍タイトル
title: "Pythonで科学計算"

# 作者情報
author: "山田 太郎"

# 出力設定
execute:
  execute_notebooks: off

# HTMLテーマ設定
html:
  favicon: images/icon.png
  logo: images/logo.png
  use_repository_button: true
```

--

### GitHubにデプロイ

https://github.com/ruoyu0088/scipybook/blob/main/.github/workflows/deploy.yml

---

## JupyterLite

- 完全にブラウザ内で実行
- 最新の **Python 3.13** 対応
- ファイルはブラウザの **IndexedDB** に保存
- セキュリティ面も安心
  * ローカルファイルアクセスができない
  * データのアップロードができない
- 遅くない(ネイティブの**6割 ~ 8割**)

--

### WASMで動くPython

* **WASM**：ブラウザ上で高速に動作するバイナリ命令形式
* **Pyodide**：PythonをWASMに移植したもの
* **JupyterLite**：Pyodide上で動くJupyterLab環境

**→**

**Write once, run anywhere**

ブラウザさえあれば動く<br>
（iOS / Android / Windows / macOS / Linux）

--

### Commands

```text
pip install jupyterlite-core jupyterlite-pyodide-kernel
jupyter lite build --contents content
```

--

<h3><svg height="65" aria-hidden="true" viewBox="0 0 24 24" version="1.1" width="64" data-view-component="true" color="white">
    <path fill="white" d="M12 1C5.923 1 1 5.923 1 12c0 4.867 3.149 8.979 7.521 10.436.55.096.756-.233.756-.522 0-.262-.013-1.128-.013-2.049-2.764.509-3.479-.674-3.699-1.292-.124-.317-.66-1.293-1.127-1.554-.385-.207-.936-.715-.014-.729.866-.014 1.485.797 1.691 1.128.99 1.663 2.571 1.196 3.204.907.096-.715.385-1.196.701-1.471-2.448-.275-5.005-1.224-5.005-5.432 0-1.196.426-2.186 1.128-2.956-.111-.275-.496-1.402.11-2.915 0 0 .921-.288 3.024 1.128a10.193 10.193 0 0 1 2.75-.371c.936 0 1.871.123 2.75.371 2.104-1.43 3.025-1.128 3.025-1.128.605 1.513.221 2.64.111 2.915.701.77 1.127 1.747 1.127 2.956 0 4.222-2.571 5.157-5.019 5.432.399.344.743 1.004.743 2.035 0 1.471-.014 2.654-.014 3.025 0 .289.206.632.756.522C19.851 20.979 23 16.854 23 12c0-6.077-4.922-11-11-11Z"></path>
</svg>Pagesで公開できる！</h3>

1. https://github.com/jupyterlite/demo の **Use this template** をクリック
2. GitHub Pagesを有効化するだけで完了！
3. `contents` フォルダを自由に変更、**Push**すると自動で反映される

https://github.com/ruoyu0088/jupyterlite/blob/main/.github/workflows/deploy.yml