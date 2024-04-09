export function Keyboard(props){

    const first_row = [
        {key:'`', shiftedKey: '~', index: 0},
        {key:'1', shiftedKey: '!', index: 1},
        {key:'2', shiftedKey: '@', index: 2},
        {key:'3', shiftedKey: '#', index: 3},
        {key:'4', shiftedKey: '$', index: 4},
        {key:'5', shiftedKey: '%', index: 5},
        {key:'6', shiftedKey: '^', index: 6},
        {key:'7', shiftedKey: '&', index: 7},
        {key:'8', shiftedKey: '*', index: 8},
        {key:'9', shiftedKey: '(', index: 9},
        {key:'0', shiftedKey: ')', index: 10},
        {key:'-', shiftedKey: '_', index: 11},
        {key:'=', shiftedKey: '+', index: 12},
    ]

    const second_row = [
        {key:'q', shiftedKey: 'Q', index: 0},
        {key:'w', shiftedKey: 'W', index: 1},
        {key:'e', shiftedKey: 'E', index: 2},
        {key:'r', shiftedKey: 'R', index: 3},
        {key:'t', shiftedKey: 'T', index: 4},
        {key:'y', shiftedKey: 'Y', index: 5},
        {key:'u', shiftedKey: 'U', index: 6},
        {key:'i', shiftedKey: 'I', index: 7},
        {key:'o', shiftedKey: 'O', index: 8},
        {key:'p', shiftedKey: 'P', index: 9},
        {key:'[', shiftedKey: '{', index: 10},
        {key:']', shiftedKey: '}', index: 11},
        {key:'\\', shiftedKey: '|', index: 12}, 
    ]

    const third_row = [
        {key:'a', shiftedKey: 'A', index: 0},
        {key:'s', shiftedKey: 'S', index: 1},
        {key:'d', shiftedKey: 'D', index: 2},
        {key:'f', shiftedKey: 'F', index: 3},
        {key:'g', shiftedKey: 'G', index: 4},
        {key:'h', shiftedKey: 'H', index: 5},
        {key:'j', shiftedKey: 'J', index: 6},
        {key:'k', shiftedKey: 'K', index: 7},
        {key:'l', shiftedKey: 'L', index: 8},
        {key:';', shiftedKey: ':', index: 9},
        {key:"\'", shiftedKey: '\"', index: 10}, 
    ]

    const fourth_row = [
        {key:'Shift', shiftedKey: 'Shift', index: 0},
        {key:'z', shiftedKey: 'Z', index: 1},
        {key:'x', shiftedKey: 'X', index: 2},
        {key:'c', shiftedKey: 'C', index: 3},
        {key:'v', shiftedKey: 'V', index: 4},
        {key:'b', shiftedKey: 'B', index: 5},
        {key:'n', shiftedKey: 'N', index: 6},
        {key:'m', shiftedKey: 'M', index: 7},
        {key:',', shiftedKey: '<', index: 8},
        {key:'.', shiftedKey: '>', index: 9},
        {key:"/", shiftedKey: '?', index: 10}, 
        {key:"Shift", shiftedKey: 'Shift', index: 11}, 
    ]


    return(
        <div className="keyboard">
            <KeyRow keys={first_row} shiftOn={props.shiftOn} keysDown={props.keysDown} 
            currentChar={props.currentChar} isShiftRequired={props.isShiftRequired} setIsShiftRequired={props.setIsShiftRequired}/>
            <KeyRow keys={second_row} shiftOn={props.shiftOn} keysDown={props.keysDown} 
            currentChar={props.currentChar} isShiftRequired={props.isShiftRequired} setIsShiftRequired={props.setIsShiftRequired}/>
            <KeyRow keys={third_row} shiftOn={props.shiftOn} keysDown={props.keysDown} 
            currentChar={props.currentChar} isShiftRequired={props.isShiftRequired} setIsShiftRequired={props.setIsShiftRequired}/>
            <KeyRow keys={fourth_row} shiftOn={props.shiftOn} keysDown={props.keysDown} 
            currentChar={props.currentChar} isShiftRequired={props.isShiftRequired} setIsShiftRequired={props.setIsShiftRequired}/>
            <Key info="spacebar" keysDown={props.keysDown} currentChar={props.currentChar} />
        </div>
    )
}

function KeyRow(props){
    
    const keys = props.keys.map(key_info => 
    <Key info={key_info} shiftOn={props.shiftOn} keysDown={props.keysDown} 
    currentChar={props.currentChar} key={key_info.index} 
    isShiftRequired={props.isShiftRequired} setIsShiftRequired={props.setIsShiftRequired}/>
    );

    return(
        <div className="keyboard-row">
            {keys}
        </div>
    )
}

function Key(props){

    let key_class = "keyboard-key";
    let key_displayed = "";
     
    
    if (props.info === "spacebar"){

        key_class += " space-bar"

        if (props.keysDown.includes(" ")){
            key_class += " active"
        }
        if (props.currentChar === " "){
            key_class += " highlighted"
        }

    } else {
        key_displayed = props.info.key;
        
        if (props.shiftOn){
            key_displayed = props.info.shiftedKey;
            props.setIsShiftRequired(false);
        } else if (props.info.shiftedKey === props.currentChar) {
            props.setIsShiftRequired(true);
        }
        
        if (props.info.key === "Shift"){
            key_class += " shift"
            if (props.isShiftRequired){
                key_class += " highlighted"
            }
        }

        if (props.keysDown.includes(key_displayed)){
            key_class += " active"
        }

        if (props.currentChar === key_displayed){
            key_class += " highlighted"
        }

    }
    

    return(
        <div className={key_class}>{key_displayed}</div>
    )
}