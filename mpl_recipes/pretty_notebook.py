from IPython.display import HTML, display
from IPython.core.magic import register_line_magic

@register_line_magic
def pretty_notebook(line):
    display(HTML("""
        <style>
        /* narrow output lines */
        .text_cell_render p {
            width: 105ex;
        }
        .text_cell_render {
            font-family: Helvetica Neue;
            font-size: 17px;
        }
        .text_cell_render code,
        .text_cell_render kbd,
        .text_cell_render pre,
        .text_cell_render samp,
        .CodeMirror,
        .output_text pre {
            font-family: Inconsolata, monospace;
            font-size: 17px;
        }
        h1, h2 {
            color: #5F452C;
        }
        h1 {
            text-decoration: underline;
        }
        h3, h4 {
            color: #333333;
        }
        h4 {
            font-style: italic;
        }
        </style>
    """))
