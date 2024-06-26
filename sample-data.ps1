#Requires -Version 5

<#
   NAME: sample-data.ps1
   DATE: 04/03/2024

.SYNOPSIS
    Generate file and folder structures for contestant search utilities

.DESCRIPTION
    Generate file and folder structures for contestant search utilities
#>

$lorum = -join @(
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et "
    "dolore magna aliqua. Tortor aliquam nulla facilisi cras fermentum. Sodales ut eu sem integer. Fusce id velit "
    "ut tortor pretium viverra suspendisse. Elementum nisi quis eleifend quam adipiscing vitae proin sagittis "
    "nisl. Cursus metus aliquam eleifend mi in. Sed turpis tincidunt id aliquet risus feugiat. Tellus in hac "
    "habitasse platea dictumst. Eu mi bibendum neque egestas congue quisque egestas. Facilisi etiam dignissim "
    "diam quis enim lobortis."
)

$path_depth = 6

$root_path = [System.Environment]::GetFolderPath('Desktop')

Write-Host "Saving folder structure in $($root_path)."

$comp_path = New-Item -ItemType Directory -Path $root_path -Name 'competition'
$folder = New-Item -ItemType Directory -Path $comp_path -Name 'milestone1'
for ($i=1; $i -le $path_depth; $i++) {
    $folder = New-Item -ItemType Directory -Path $folder -Name "f$($i)"
    foreach ($file in ('john', 'paul', 'george', 'ringo')) {
        $cmd_args = @{
            ItemType = 'File'
            Path = $folder
            Name = "f$($i)-$($file).txt"
            Value = "f$($i)-$($file)`r`n`r`n$($lorum)"
        }
        $null = New-Item @cmd_args
    }
}

$folder = New-Item -ItemType Directory -Path $comp_path -Name 'milestonex'
for ($i=1; $i -le $path_depth; $i++) {
    if ($i -eq $path_depth) {
        $null = New-Item -ItemType Junction -Path "$($folder.FullName)\f6" -Target "$($folder.FullName)"

    } else {
        $folder = New-Item -ItemType Directory -Path $folder -Name "f$($i)"
        foreach ($file in ('john', 'paul', 'george', 'ringo')) {
            $cmd_args = @{
                ItemType = 'File'
                Path = $folder
                Name = "f$($i)-$($file).txt"
                Value = "f$($i)-$($file)`r`n`r`n$($lorum)"
            }
            $null = New-Item @cmd_args
        }
    }
}

