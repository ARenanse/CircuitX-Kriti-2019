1. Find Positions where input is present
2. Then find uniquee Initial Positions
3. Then from step 2, create all possible inputs
4. Put the corrseponding inputs in the input columns of the initial inputs
5. Forward Pass over the matrix with the input as the current boolean states of each physical input
    a) Initial Evaluation directly from inputs
    b) INITIALIZE THE INPUT FOR THE NOT GATES
    c) Initiate an Infinite While Loop:
        
        1.) PUT OUTPUT TO NEXT INPUTS
        2.) SIMILARILY, UPDATE THE input_loc BOOL TABLE
        3.) For long term memory, initiate a 'cache'
        4.) Check loop breaking condition, which is if the output 111 (Yellow) is reached
        5.) If not, then calculate next outputs
        
    d)At this point, we have an output for the corresponding input.
6. Display the output