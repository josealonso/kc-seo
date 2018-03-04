import '../css/main.css';
import '../css/grid.css';
import '../css/font-awesome.min.css';

import './menu';

import './animations';

import './validate';

import { drawMessages, createContactMsg, getMessages, deleteMessages } from './ajax';

var messages = [];

getMessages();