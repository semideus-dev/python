------------------------------------------------------------------------

### High-Level Languages

A high-level language is a programming language with strong **abstraction** from the details of the computer. It uses natural language elements, easier to use, and automates area of computer system such as *memory management*, *garbage collection* etc. This makes the development process faster, simpler and more understandable than a low-level language.

### Interpreter

The software by which the conversion of the high-level instructions is performed line-by-line to machine code is known as an **Interpreter**. The execution is stopped immediately if an error is found on any line. This is helpful in development environments as frequent changes are required making the compiling method extremely slow.

It was designed to rectify the compiler's problems as long programs might take hours to compile and runtime errors will only slow down the development significantly.

Languages which use an interpreter are called Interpreted Languages. Examples include Python, Javascript, Ruby etc.

Also see [Complier vs Interpreter](/Resources/Differences#Complier%20vs%20Interpreter)

### Compiler

It is a **translating** software that converts a program written in a high-level language to machine code. The speed of a compiler is generally **slower** than most system softwares as the entire program is compiled all at once however the end output program is much faster than Interpreted programs.

It breaks down the code character-by-character into a series of tokens (keywords, identifiers, operators etc.). These tokens are then **parsed** for syntax analysis where errors checking takes place. Next step is type checking, also known as **semantic analysis**. This also includes handling of incorrect functions, undeclared variables etc.

Penultimate step is where the code is actually converted into machine code before finally optimizing it for efficient runtime.

Languages which use a compiler are called Complied Languages. Examples include C#,  C++, Rust, Java etc.

Also see [Complier vs Interpreter](/Resources/Differences#Complier%20vs%20Interpreter)
