import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSun, faMoon } from '@fortawesome/free-solid-svg-icons';
import classes from './DarkLight.module.css';

const DarkLight = ({ toggleDarkMode, isDarkMode }) => {
  return (
    <button onClick={toggleDarkMode} className={classes.darkLightButton}>
      <FontAwesomeIcon icon={isDarkMode ? faSun : faMoon} className={classes.icon} />
    </button>
  );
};

export default DarkLight;
