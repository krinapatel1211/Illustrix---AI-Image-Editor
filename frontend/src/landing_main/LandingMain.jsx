import React from 'react';
import { Layout, Typography, Button } from 'antd';
import { Col, Row } from 'antd';
import ParticleBG from '../particle_bg/ParticleBG';
import LoginModal from '../modals/LoginModal';
import SignupModal from '../modals/SignupModal';

const { Content, Footer } = Layout;
const { Title } = Typography;

const heroImage = 'landing_hero.png'

const contentStyle = {
    textAlign: 'left',
    // minHeight: 768,
    lineHeight: '120px',
    padding: '220px 50px 220px 120px',
  };

const imageStyle = {
    marginTop: '120px',
}

const rowStyle = {
    textAlign: 'center',
    verticalAlign: 'center',
    maxheight: '100vh',
}

class LandingMain extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
          login_modal_open: false,
          signup_modal_open: false
        };
    }

    updateLoginModal(flag) {
        this.setState({login_modal_open: flag});
    }

    updateSignupModal(flag) {
        this.setState({signup_modal_open: flag});
    }

    render() {
        return (
        <Row style={rowStyle}>
            <ParticleBG />
            <LoginModal 
                login_modal_open={this.state.login_modal_open} 
                title="Login" 
                updateLoginModal={this.updateLoginModal.bind(this)} 
            />
            <SignupModal 
                signup_modal_open={this.state.signup_modal_open} 
                title="Sign up" 
                updateSignupModal={this.updateSignupModal.bind(this)}
                updateLoginModal={this.updateLoginModal.bind(this)} 
            />
            <Col span={12}>
                <Content style={contentStyle}>
                    <Title level={1}>Transform Your Images with <br/>AI - Powered Editing.</Title>
                    <Title level={4}>Experience the Next Level of Image Editing: Illistrix Harnesses the Power of Artificial Intelligence for Effortless Transformations.</Title>
                    <Button onClick={()=> this.updateLoginModal(true)} type="primary" size="large" className="hero-cta-button">
                        Login
                    </Button>
                    <Button onClick={()=> this.updateSignupModal(true)} type="dafault" size="large" className="hero-cta-button">
                        Sign up
                    </Button>
                </Content>
            </Col>
            <Col span={12}>
                <img src={heroImage} alt="Illistrix in action" style={imageStyle} className="hero-image" />
            </Col>
            <Col span={24}>
                <Footer style={{ textAlign: 'center', background: 'transparent' }}>Copyright © Illustrix, 2023. All rights reserved.</Footer>
            </Col>
        </Row>
        )
    }
}
  
export default LandingMain;