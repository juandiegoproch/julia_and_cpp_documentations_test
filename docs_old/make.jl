using Documenter
using DocumenterInterLinks
include(joinpath(@__DIR__, "..", "src", "test_julia.jl"))
using .test_julia  # your module

makedocs(
    sitename = "test_julia Documentation",
    modules = [test_julia],
    format = Documenter.HTML(repolink = ""),
    plugins = [InterLinks()],
    remotes = nothing
)
