module test_julia
    const LIBPATH = joinpath(@__DIR__, "..", "csrc", "libadd.so")
    """
    Add two numbers by calling C extern

    # Arguments
    - `x::Int8`: First number
    - `y::Int8`: Second number

    # Returns
    - `Int`: Sum of `x` and `y`


    Calls: [`sum`](@extref `sum`)
    """
    function testJuliaFunction(x::Int8, y::Int8)::Int
        return ccall((:sum,LIBPATH),Int,(Int8, Int8),x,y)

    end 
end
# module test_julia
