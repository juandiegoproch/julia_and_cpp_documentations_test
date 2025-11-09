using Documenter
using DocumenterInterLinks
include(joinpath(@__DIR__, "..", "src", "test_julia.jl"))
using .test_julia  # your module

links = InterLinks( "libadd" => "http://127.0.0.1:8082/")

makedocs(
    sitename = "Test JuliaDocs",
    modules = [test_julia],
    format = Documenter.HTML(repolink = ""),
    plugins = [links],
    remotes = nothing
)
