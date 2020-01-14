$ErrorActionPreference = 'Stop'

Function Convert-CsvInBatch
{
	[CmdletBinding()]
	Param
	(
		[Parameter(Mandatory=$true)][String]$Folder
	)
	$ExcelFiles = Get-ChildItem -Path $Folder -Filter *.xlsx -Recurse

	$excelApp = New-Object -ComObject Excel.Application
	$excelApp.DisplayAlerts = $false

	$ExcelFiles | ForEach-Object {
		$workbook = $excelApp.Workbooks.Open($_.FullName)
		$csvFilePath = $_.FullName -replace "\.xlsx$", ".csv"
		$workbook.SaveAs($csvFilePath, [Microsoft.Office.Interop.Excel.XlFileFormat]::xlCSV)
		$workbook.Close()
	}

	# Release Excel Com Object resource
	$excelApp.Workbooks.Close()
	$excelApp.Visible = $true
	Start-Sleep 5
	$excelApp.Quit()
	[System.Runtime.Interopservices.Marshal]::ReleaseComObject($excelApp) | Out-Null
}

#
# 0. Prepare the folder path which contains all excel files
$FolderPath = "./"

Convert-CsvInBatch -Folder $FolderPath
