if exists("b:current_syntax")
    finish
endif

syntax match mmiFunctionLiteral /->/
syntax match mmiOtherSymbols /[|().,:]/

syntax match mmiType /\<[A-Z][a-z]*\>/
syntax match mmiNamedComma /#\<\w\+\>/
syntax match mmiGenericParameter /@\<\w\+\>/

syntax keyword mmiTypeKeywords datatype elemtype

highlight link mmiFunctionLiteral Operator
highlight link mmiTypeIndicator Operator
highlight link mmiOtherSymbols Operator
highlight link mmiTypeKeywords Keyword
highlight link mmiType Type
highlight link mmiNamedComma Function
highlight link mmiGenericParameter PreProc

let b:current_syntax = "mmi"
