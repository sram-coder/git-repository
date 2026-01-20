import React from 'react';
import { Navbar, Container } from 'react-bootstrap';
import {ReactComponent as Logo} from '../images/logo.svg';
const navbarStyle = {
  backgroundColor: 'efe0e0',
};

const Header = ({ title }) => {
  return (
    <Navbar style={navbarStyle} data-bs-theme="light">
      <Container>
        <Logo style={{maxWidth:'20rem', maxHeight: '4rem'}}/>
      </Container>
    </Navbar>
  );
};

export default Header;
