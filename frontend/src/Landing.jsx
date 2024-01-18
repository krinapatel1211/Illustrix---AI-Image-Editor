import 'antd/dist/reset.css';
import { Layout, Space, ConfigProvider } from 'antd';
import LandingHeader from './landing_header/LandingHeader';
import LandingMain from './landing_main/LandingMain'

const config= {
  token: {
    colorPrimary: '#0E8388',
    colorBgBase: '#2C3333',
    colorText: '#CBE4DE',
    colorBorder: '#CBE4DE',
    colorIcon: '#CBE4DE',
  },
};

const layoutStyel = {
  background: 'transparent',
  height: '100vh',
}

function Landing() {
  return (
    <ConfigProvider 
    theme={config}
    >
      <Space direction="vertical" style={{ width: '100%', height: '100%' }} size={[0, 48]}>
        <Layout style={layoutStyel}>
          <LandingHeader ></LandingHeader>
          <LandingMain></LandingMain>
        </Layout>
      </Space>
    </ConfigProvider>
  );
}

export default Landing;
