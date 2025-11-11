# Mixed C++/Julia Documentation PoC

This repo demonstrates a way to document Julia/C++ projects wich relies on Sphynx to parse Doxygen-generated XML files to generate a Sphynx documentation that contains adequate inventory files. The Julia Documenter.jl is then used with DocumenterInterlinks to produce a final Julia API documentation that links to the C++ api functions it uses. 

# A brief tutorial

We will create a new function for libadd (sub(char,char)) and link it to julia, while maintaining appropiate documentation.

# Adding a new Julia/C++ documented function in detail:

We will first create the definition of the function in csrc/libadd.c and *important* its declaration in libadd.h. Failing to declare and document the function in an adequate header will make it invisible to sphynx. This is due to the way that sphinx handles potential duplicate documentation in headers and source files.

**libadd.c**
```
extern int sub(char x, char y){
    return (int)x - (int)y;
}
```
**libadd.h**
```
/**
 * Subtract two int8 numbers
 * \f[ x - y \f]
 * @param x First number
 * @param y Second number
 * @return diff
 */
extern int sub(char x, char y)
```

We will then add appropiate doxygen documentation.

```
extern int sub(char x, char y){
    return (int)x - (int)y;
}
```

After doing this, we have to declare the function in sphynx's documentation so that it knows where to render it. For this, go to **docs/index.rst** and add `sub` to the C API documentation.

```
.. doxygenfunction:: sub
   :project: libadd
```

You could now run doxygen on the project root and `make html` in docs/ to see the sphynx side. It should contain the documentation for the newly added `sub` function.

```
doxygen
cd docs
make html
```
After this, you can view the sphinx documentation at docs/_build/html/index.html. Now we have to create a julia function that consumes `sub` and document it.
For the next steps you should deploy it so that juliadocs can see the inventory file. You can deploy it locally by running 

```
cd docs/_build/html
python -m http.server 8082
```

Go to src/test_julia.jl and add a new function to the module
```
    """
    Subtracts two numbers 

    # Arguments
    - `x::Int8`: First number
    - `y::Int8`: Second number

    \$x - y\$

    # Returns
    - `Int`: Sum of `x` and `y`

    Calls: [`sub`](@extref `sub`)
    """
    function testJuliaSubtract(x::Int8, y::Int8)::Int
        return ccall((:sub,LIBPATH),Int,(Int8, Int8),x,y)
    end 
```
Note how you can refer to the c function `sub` via an @extref. This will link appropiatelly with the symbols defined in Doxygen.

Add the julia function to the julia manual by adding it to the @docs segment in julia_docs/src/index.md

```
test_julia.testJuliaSubtract
```

Then, on the julia_docs/ folder run
```
julia make.jl
```

Which should build the new documentation. After that you can host it as before or directly access via 

# Adding a new Julia/C++ documented function in practice:

You should be able to add julia/c++ functions by simply writing them with their docstring and writing an entry for each in the index.rst file and the julia index.md. To run all the build logistics and obtain a running documentation at localhost, you can use the spin_docs.sh file in the top level domain of this repo. To recap:

1) Write the C function and docstring
3) Add an entry in docs/index.rst for the C function
2) Write the Julia function and docstring, refering to C with @extref semantics
4) Add an entry in julia_docs/src/index.md for the julia function

It should be obvious that the overhead is minimal, as to propperly document both functions you had to do the same anyways. The bonus is you can now reference C bindings from julia with ease.

# Figures and LaTex in C

To add $`\LaTeX`$ to c functions, just add `\f[ <your-latex-here> \f]` in the docstring. 

To add figures, add your figures in the doxy_docs/images path and reference them by name in the docstring `\image HTML fig1.png`

They will be automatically and correctly exported to Sphynx through Breathe.

# Figures and LaTex in Julia

To add $`\LaTeX`$ to Julia functions just add `\$x - y\$` in the docstring. 

To add figures to julia functions, put the source images in julia_docs/src/assets and reference them using normal markdown syntax `![Illustration of subtraction](assets/fig2.png)`