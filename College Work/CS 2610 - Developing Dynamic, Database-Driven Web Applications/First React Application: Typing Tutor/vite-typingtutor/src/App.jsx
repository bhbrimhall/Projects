import { useEffect, useState } from 'react'
import { Phrase } from './Phrase'
import { Keyboard } from './Keyboard'


export function App() {
  const [shiftOn, setShift] = useState(false);
  const [keysDown, setKeysDown] = useState([]);
  const [phraseIndex, setPhraseIndex] = useState(0);
  const [completedPhrase, setCompletedPhrase] = useState("");
  const [currentChar, setCurrentChar] = useState("");
  const [remainingPhrase, setRemainingPhrase] = useState("");
  const [isShiftRequired, setIsShiftRequired] = useState(false);
  
  const phrase_list = [
    "The FitnessGram Pacer Test is a multistage aerobic capacity test that progressively gets more difficult as it continues.",
    "The 20 meter pacer test will begin in 30 seconds. Line up at the start.",
    "The running speed starts slowly, but gets faster each minute after you hear this signal.",
    "[beep]",
    "A single lap should be completed each time you hear this sound.",
    "Remember to run in a straight line, and run as long as possible.",
    "The second time you fail to complete a lap before the sound, your test is over.",
    "The test will begin on the word start. On your mark, get ready, start."
  ]

  
  function editKeysDown(){
    const keyDownFunc = (e) => {
      if (e.repeat) return;
      setKeysDown(oldKeysDown => {
        let a = [...oldKeysDown]
        a.push(e.key);
        return a;
      });
      if (e.key === "Shift"){
        setShift(true);
      }
    }
    window.addEventListener("keydown", keyDownFunc);
    
    const keyUpFunc = (e) => {
      setKeysDown(oldKeysDown => {
        let a = [...oldKeysDown]
        a.splice(oldKeysDown.indexOf(e.key), 1)
        return a;
      });
      if (e.key === "Shift"){
        setShift(false);
      }
    }
    window.addEventListener("keyup", keyUpFunc);
  }

  useEffect(editKeysDown, []);


  function setUpPhrase(){
    setCompletedPhrase("");
    setCurrentChar(phrase_list[phraseIndex][0]);
    setRemainingPhrase(phrase_list[phraseIndex].slice(1));
  }  

  function checkTypedKeys(){

    if (keysDown.includes(currentChar)){
      if (remainingPhrase === ""){
        if (phraseIndex + 1 === phrase_list.length)
          setPhraseIndex(0)
        else{
          setPhraseIndex(phraseIndex + 1);
        }
      } else {
        setCompletedPhrase(completedPhrase + currentChar);
        setCurrentChar(remainingPhrase[0]);
        setRemainingPhrase(remainingPhrase.slice(1))
      }
    }



  }

  useEffect(setUpPhrase, [phraseIndex])
  useEffect(checkTypedKeys, [keysDown])

  return (
    <main className='content'>
        <Phrase completedPhrase={completedPhrase} remainingPhrase={remainingPhrase} currentChar={currentChar}/>
        <Keyboard shiftOn={shiftOn} keysDown={keysDown} currentChar={currentChar} isShiftRequired={isShiftRequired} 
        setIsShiftRequired={setIsShiftRequired} />
    </main>
  )
}
