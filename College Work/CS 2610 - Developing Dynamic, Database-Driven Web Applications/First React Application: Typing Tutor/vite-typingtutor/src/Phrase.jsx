export function Phrase(props){
    return(
        <div className="phrase">
            <span className="typed-phrase">{props.completedPhrase}</span>
            <span className="pointer">{props.currentChar}</span>
            {props.remainingPhrase}
        </div>
    )
}