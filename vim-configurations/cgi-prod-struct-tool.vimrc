" SV imPROVED
set nocompatible

filetype on 		" Do not detect the filetype that I am working with 

set number      " Enables word numbering
set relativenumber  " Sets relative number lines

set lbr!		" Enables word wrapping

syntax enable		" Enables syntax highlighting
syn on!			" Enables automatic syntax highlighting for the specific file

colorscheme gruvbox " This sets the default theme as novum
set notermguicolors
set background gruvbox

" Sets the font, style and size
if has ('gui_running')
	set guifont=Consolas:h22
endif

set tabstop=4 		" Sets the tabstop to increment by 4

set shiftwidth=4	" Sets the tab to use spaces as its more stable	

set expandtab		" Increments by 4 when pressed
