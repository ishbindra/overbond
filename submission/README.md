Ishmeet Bindra:
Please refer to the Overbond-documentation.doc

Problem Statement:

BondYield comparisons between similar corporate and government bonds. Given a JSON file which will define an array of bond objects (of arbitrary size), the requirement is to create a command-line tool to calculate the spread between each corporate bond and the nearest government bond benchmark, save these results in a JSON file, and express the spread in basis points, or bps. If any properties are missing from a bond object, do not include it in your calculations or output.
Points to be considered as follows:
Calculate Spread (difference between the yield of a corporate bond and its government bond benchmark)
In case of a tie for closest government bond by tenor, break the tie by choosing the government bond with the largest amount outstanding.
Convert the difference to basis points (scale of 100)

Files in this repository:

Following are the files in this repo:
solution_script.py: This is the python script file containing the solution. 
testing_script.py: File for automated test scripts. 
Docker:  Directory containing the file required for building a docker image. 
sample_input.json
sample_output.json 

Solution Approach:
Approach for solving the problem included understanding the business problem first. Understanding the details on how to convert the business requirements to technical design. Below are the steps, which were created as a pseudo programming steps to guide during the code. Please note that these steps were changed during the coding and also during the testing phase. These steps will give you an understanding of the approach. 

Read the arguments - Input and Output filenames
Read the input json file and then convert it into a dataframe
Remove Null Values
Convert Tenor and Yield to Float for calculation
Split the dataset by type - Corporate and Government
Iterate through the Corporate Dataframe to find the nearest government bond in terms of tenure
Find the difference in yield of government bonds and corporate bonds    
Format the output
Create test cases 
Write an automated test case program


Steps to Run
The code can be run using the following 2 options. Option:1 Command line is tested. Option:2 DockerFile is tested too, but I recommend you to use option:1.

 Command Line Interface
Please run using the following command using Python 3.6
python  Solution_Script.py sample_input.json sample_out.json
Dockerfile 
Run the following 2 commands
docker build -t overbond-img .
docker run overbond-img
Test Case Creation Approach
---------------------
Test scenario :1
 - If Type is not Corporate or government
---------------------

{
	"data": [{
			"id": "c1",
			"type": "private",
			"tenor": "10.3 years",
			"yield": "5.30%",
			"amount_outstanding": 1200000
		},
		{
			"id": "g1",
			"type": "government",
			"tenor": "9.4 years",
			"yield": "3.70%",
			"amount_outstanding": 2500000
		},
		{
			"id": "c2",
			"type": "corporate",
			"tenor": "13.5 years",
			"yield": "4.3%",
			"amount_outstanding": 1100000
		},
		{
			"id": "g2",
			"type": "government",
			"tenor": "12.0 years",
			"yield": "4.80%",
			"amount_outstanding": 1750000
		}
	]
}




output:


{
  "data": [
    {
      "corporate_bond_id": "c2”,
      "government_bond_id": "g2”,
      "spread_to_benchmark": “50 bps"
    }
  ]
}




---------------------
Test scenario :2
 - If Fields are null
---------------------
Test scenario :2.1
 - If id is null

{
 "data": [{
 "id": null,
 "type": "corporate",
 "tenor": "10.3 years",
 "yield": "5.30%",
 "amount_outstanding": 1200000
 },
 {
 "id": "g1",
 "type": "government",
 "tenor": "9.4 years",
 "yield": "3.70%",
 "amount_outstanding": 2500000
 },
 {
 "id": "c2",
 "type": "corporate",
 "tenor": "13.5 years",
 "yield": "4.3%",
 "amount_outstanding": 1100000
 },
 {
 "id": "g2",
 "type": "government",
 "tenor": "12.0 years",
 "yield": "4.80%",
 "amount_outstanding": 1750000
 }
 ]
}


output:



{

  "data": [

    {

      "corporate_bond_id": "c2”,

      "government_bond_id": "g2”,

      "spread_to_benchmark": “50 bps"

    }

  ]

}





---------------------
Test scenario :2.2
 - If Type is null

{
 "data": [{
 "id": "c1",
 "type": null,
 "tenor": "10.3 years",
 "yield": "5.30%",
 "amount_outstanding": 1200000
 },
 {
 "id": "g1",
 "type": "government",
 "tenor": "9.4 years",
 "yield": "3.70%",
 "amount_outstanding": 2500000
 },
 {
 "id": "c2",
 "type": "corporate",
 "tenor": "13.5 years",
 "yield": "4.3%",
 "amount_outstanding": 1100000
 },
 {
 "id": "g2",
 "type": "government",
 "tenor": "12.0 years",
 "yield": "4.80%",
 "amount_outstanding": 1750000
 }
 ]
}


output:

 "data": [{
 "id": "c1",
 "type": "corporate",
 "tenor": null,
 "yield": "5.30%",
 "amount_outstanding": 1200000
 },
 {
 "id": "g1",
 "type": "government",
 "tenor": "9.4 years",
 "yield": "3.70%",
 "amount_outstanding": 2500000
 },
 {
 "id": "c2",
 "type": "corpora

{

  "data": [

    {

      "corporate_bond_id": "c2”,

      "government_bond_id": "g2”,

      "spread_to_benchmark": “50 bps"

    }

  ]

}



---------------------
Test scenario :2.3
 - If tenor is null

{
te",
 "tenor": "13.5 years",
 "yield": "4.3%",
 "amount_outstanding": 1100000
 },
 {
 "id": "g2",
 "type": "government",
 "tenor": "12.0 years",
 "yield": "4.80%",
 "amount_outstanding": 1750000
 }
 ]
}

output:



{

  "data": [

    {

      "corporate_bond_id": "c2”,

      "government_bond_id": "g2”,

      "spread_to_benchmark": “50 bps"

    }

  ]

}



---------------------
Test scenario :2.4
 - If amount_outstanding is null

{
 "data": [{
 "id": "c1",
 "type": "corporate",
 "tenor": null,
 "yield": "5.30%",
 "amount_outstanding": null
 },
 {
 "id": "g1",
 "type": "government",
 "tenor": "9.4 years",
 "yield": "3.70%",
 "amount_outstanding": 2500000
 },
 {
 "id": "c2",
 "type": "corporate",
 "tenor": "13.5 years",
 "yield": "4.3%",
 "amount_outstanding": 1100000
 },
 {
 "id": "g2",
 "type": "government",
 "tenor": "12.0 years",
 "yield": "4.80%",
 "amount_outstanding": 1750000
 }
 ]
}

output:



{

  "data": [

    {

      "corporate_bond_id": "c2”,

      "government_bond_id": "g2”,

      "spread_to_benchmark": “50 bps"

    }

  ]

}




---------------------
Test scenario :2.5
 - If Yeild is null


{
 "data": [{
 "id": "c1",
 "type": "corporate",
 "tenor": "10.3 years",
 "yield": "5.30%",
 "amount_outstanding": 1200000
 },
 {
 "id": "g1",
 "type": "government",
 "tenor": "9.4 years",
 "yield": "3.70%",
 "amount_outstanding": 2500000
 },
 {
 "id": "c2",
 "type": "corporate",
 "tenor": "13.5 years",
 "yield": null,
 "amount_outstanding": 1100000
 },
 {
 "id": "g2",
 "type": "government",
 "tenor": "12.0 years",
 "yield": "4.80%",
 "amount_outstanding": 1750000
 }
 ]
}

output:



{

  "data": [

    {

      "corporate_bond_id": "c2”,

      "government_bond_id": "g2”,

      "spread_to_benchmark": “50 bps"

    }

  ]

}


------------------------
Test scenario :3
 --If Yeild is 0% we would still process it.

{
 "data": [{
 "id": "c1",
 "type": "corporate",
 "tenor": "10.3 years",
 "yield": "0.00%",
 "amount_outstanding": 1200000
 },
 {
 "id": "g1",
 "type": "government",
 "tenor": "9.4 years",
 "yield": "3.70%",
 "amount_outstanding": 2500000
 },
 {
 "id": "c2",
 "type": "corporate",
 "tenor": "13.5 years",
 "yield": "4.3%",
 "amount_outstanding": 1100000
 },
 {
 "id": "g2",
 "type": "government",
 "tenor": "12.0 years",
 "yield": "4.80%",
 "amount_outstanding": 1750000
 }
 ]
}

Output:

{

  "data": [

    {

      "corporate_bond_id": "c2”,

      "government_bond_id": "g2”,

      "spread_to_benchmark": “50 bps"

    }

  ]

}



------------------------
Test scenario:4
--If there is a tie for closest government bond by tenor, break the tie by choosing the government bond with the largest amount outstanding.


{
 "data": [{
 "id": "c1",
 "type": "corporate",
 "tenor": "10 years",
 "yield": "5.30%",
 "amount_outstanding": 1200000
 },
 {
 "id": "g1",
 "type": "government",
 "tenor": "9.4 years",
 "yield": "3.70%",
 "amount_outstanding": 2500000
 },
 {
 "id": "c2",
 "type": "corporate",
 "tenor": "13.5 years",
 "yield": null,
 "amount_outstanding": 1100000
 },
 {
 "id": "g2",
 "type": "government",
 "tenor": "10.6 years",
 "yield": "4.80%",
 "amount_outstanding": 1750000
 }
 ]
}

Output:

{

  "data": [

    {

      "corporate_bond_id": "c1”,

      "government_bond_id": "g1”,

      "spread_to_benchmark": “160 bps"

    }

  ]

}



------------------------
Test scenario :5
--no data in the file


{
 "data": [
 ]
}

Output:

{

  "data": [

    {

      "corporate_bond_id": "c1”,

      "government_bond_id": "g1”,

      "spread_to_benchmark": “160 bps"

    }

  ]

}




---------------------
Test scenario :6
 - If Fields are missing
---------------------
Test scenario :6.1
 - If id is missing

{
 "data": [{
 
 "type": "corporate",
 "tenor": "10.3 years",
 "yield": "5.30%",
 "amount_outstanding": 1200000
 },
 {
 "id": "g1",
 "type": "government",
 "tenor": "9.4 years",
 "yield": "3.70%",
 "amount_outstanding": 2500000
 },
 {
 "id": "c2",
 "type": "corporate",
 "tenor": "13.5 years",
 "yield": "4.3%",
 "amount_outstanding": 1100000
 },
 {
 "id": "g2",
 "type": "government",
 "tenor": "12.0 years",
 "yield": "4.80%",
 "amount_outstanding": 1750000
 }
 ]
}

output:



{

  "data": [

    {

      "corporate_bond_id": "c2”,

      "government_bond_id": "g2”,

      "spread_to_benchmark": “50 bps"

    }

  ]

}



---------------------
Test scenario :6.2
 - If Type is missing

{
 "data": [{
 "id": "c1",
 "tenor": "10.3 years",
 "yield": "5.30%",
 "amount_outstanding": 1200000
 },
 {
 "id": "g1",
 "type": "government",
 "tenor": "9.4 years",
 "yield": "3.70%",
 "amount_outstanding": 2500000
 },
 {
 "id": "c2",
 "type": "corporate",
 "tenor": "13.5 years",
 "yield": "4.3%",
 "amount_outstanding": 1100000
 },
 {
 "id": "g2",
 "type": "government",
 "tenor": "12.0 years",
 "yield": "4.80%",
 "amount_outstanding": 1750000
 }
 ]
}


output:



{

  "data": [

    {

      "corporate_bond_id": "c2”,

      "government_bond_id": "g2”,

      "spread_to_benchmark": “50 bps"

    }

  ]

}


---------------------
Test scenario :6.3
 - If tenor is Missing

{
 "data": [{
 "id": "c1",
 "type": "corporate",
 "yield": "5.30%",
 "amount_outstanding": 1200000
 },
 {
 "id": "g1",
 "type": "government",
 "tenor": "9.4 years",
 "yield": "3.70%",
 "amount_outstanding": 2500000
 },
 {
 "id": "c2",
 "type": "corporate",
 "tenor": "13.5 years",
 "yield": "4.3%",
 "amount_outstanding": 1100000
 },
 {
 "id": "g2",
 "type": "government",
 "tenor": "12.0 years",
 "yield": "4.80%",
 "amount_outstanding": 1750000
 }
 ]
}



output:



{

  "data": [

    {

      "corporate_bond_id": "c2”,

      "government_bond_id": "g2”,

      "spread_to_benchmark": “50 bps"

    }

  ]

}


---------------------
Test scenario:6.4
 - If amount_outstanding Missing

{
 "data": [{
 "id": "c1",
 "type": "corporate",
 "tenor": "9.4 years",
 "yield": "5.30%",
 
 },
 {
 "id": "g1",
 "type": "government",
 "tenor": "9.4 years",
 "yield": "3.70%",
 "amount_outstanding": 2500000
 },
 {
 "id": "c2",
 "type": "corporate",
 "tenor": "13.5 years",
 "yield": "4.3%",
 "amount_outstanding": 1100000
 },
 {
 "id": "g2",
 "type": "government",
 "tenor": "12.0 years",
 "yield": "4.80%",
 "amount_outstanding": 1750000
 }
 ]
}

output:



{

  "data": [

    {

      "corporate_bond_id": "c2”,

      "government_bond_id": "g2”,

      "spread_to_benchmark": “50 bps"

    }

  ]

}


---------------------
Test scenario :6.5
 - If Yeild is Missing

{
 "data": [{
 "id": "c1",
 "type": "corporate",
 "tenor": "10.3 years",
 "amount_outstanding": 1200000
 },
 {
 "id": "g1",
 "type": "government",
 "tenor": "9.4 years",
 "yield": "3.70%",
 "amount_outstanding": 2500000
 },
 {
 "id": "c2",
 "type": "corporate",
 "tenor": "13.5 years",
 "yield": "4.7%",
 "amount_outstanding": 1100000
 },
 {
 "id": "g2",
 "type": "government",
 "tenor": "12.0 years",
 "yield": "4.80%",
 "amount_outstanding": 1750000
 }
 ]
}

output:



{

  "data": [

    {

      "corporate_bond_id": "c2”,

      "government_bond_id": "g2”,

      "spread_to_benchmark": “50 bps"

    }

  ]

}


---------------------
Test scenario :7.1
 - If Corporate is missing

{
 "data": [
 {
 "id": "g1",
 "type": "government",
 "tenor": "9.4 years",
 "yield": "3.70%",
 "amount_outstanding": 2500000
 },
 {
 "id": "g2",
 "type": "government",
 "tenor": "12.0 years",
 "yield": "4.80%",
 "amount_outstanding": 1750000
 }
 ]
}

output:



{

  "data": [

    

  ]

}

---------------------
Test scenario:7.2
 - If the Government is missing

{
 "data": [
 {
 "id": "c1",
 "type": "corporate",
 "tenor": "9.4 years",
 "yield": "3.70%",
 "amount_outstanding": 2500000
 },
 {
 "id": "c2",
 "type": "corporate",
 "tenor": "12.0 years",
 "yield": "4.80%",
 "amount_outstanding": 1750000
 }
 ]
}

output:

{

  "data": [

    

  ]

}









