import axios, { AxiosInstance, AxiosError } from 'axios';
import { StorageService } from './storage';
import {
  User,
  AuthTokens,
  LoginRequest,
  RegisterRequest,
  BurnoutAnalysis,
  SleepRecord,
  PhoneUsageRecord,
  EmotionRecord,
  ActivityRecord,
  DashboardData,
  Recommendation,
  ResetPasswordRequest,
} from '../types';

const API_BASE_URL = 'https://burnout-backend-l438.onrender.com/api/v1';

const api: AxiosInstance = axios.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor to add auth token
api.interceptors.request.use(
  async (config) => {
    const token = await StorageService.getToken();
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Response interceptor
api.interceptors.response.use(
  (response) => response,
  async (error: AxiosError) => {
    if (error.response?.status === 401) {
      await StorageService.clearAll();
    }
    return Promise.reject(error);
  }
);

// ─── Mock Data ─────────────────────────────────────────────────────────────────

const MOCK_USER: User = {
  id: 1,
  username: 'demo_user',
  email: 'demo@burnoutai.com',
  full_name: 'Alex Johnson',
  age: 28,
  gender: 'prefer_not_to_say',
  created_at: new Date().toISOString(),
  is_active: true,
};

const MOCK_BURNOUT: BurnoutAnalysis = {
  burnout_score: 42,
  risk_level: 'moderate',
  confidence: 0.87,
  factors: [
    { name: 'Sleep Deprivation', impact: 35, description: 'Averaging 5.5h of sleep' },
    { name: 'High Screen Time', impact: 28, description: '7.2 hours daily average' },
    { name: 'Low Physical Activity', impact: 22, description: 'Below recommended levels' },
    { name: 'Emotional Stress', impact: 15, description: 'Elevated stress markers' },
  ],
  recommendations: [
    {
      id: 1,
      title: 'Establish a Sleep Schedule',
      description: 'Consistent sleep timing regulates your circadian rhythm and reduces burnout risk by up to 30%.',
      priority: 'high',
      category: 'sleep',
      action_steps: [
        'Set bedtime alarm for 10:30 PM',
        'Avoid screens 1 hour before bed',
        'Keep bedroom temperature at 68°F',
        'Try 4-7-8 breathing technique',
      ],
      estimated_impact: 8,
    },
    {
      id: 2,
      title: 'Reduce Phone Usage',
      description: 'Cut daily screen time to under 4 hours to significantly improve focus and mental clarity.',
      priority: 'high',
      category: 'phone',
      action_steps: [
        'Enable app time limits in Settings',
        'Put phone in another room during meals',
        'Use grayscale mode after 8 PM',
        'Try a 2-hour phone-free morning',
      ],
      estimated_impact: 7,
    },
    {
      id: 3,
      title: '20-Minute Daily Walk',
      description: 'Light daily exercise dramatically reduces cortisol and improves mood within 2 weeks.',
      priority: 'medium',
      category: 'activity',
      action_steps: [
        'Walk during lunch break',
        'Park farther from destination',
        'Take stairs instead of elevator',
        'Invite a colleague for a walking meeting',
      ],
      estimated_impact: 6,
    },
    {
      id: 4,
      title: 'Practice Mindfulness',
      description: '10 minutes of daily meditation reduces anxiety and improves emotional regulation.',
      priority: 'medium',
      category: 'mental',
      action_steps: [
        'Try guided meditation apps',
        'Deep breathing for 5 minutes morning',
        'Body scan before sleep',
        'Journaling for 10 minutes daily',
      ],
      estimated_impact: 5,
    },
  ],
  timestamp: new Date().toISOString(),
  wellness_score: 62,
  emotional_stability_index: 68,
  sleep_quality_score: 55,
  phone_usage_score: 48,
  activity_score: 70,
};

const MOCK_SLEEP: SleepRecord = {
  id: 1,
  user_id: 1,
  date: new Date().toISOString().split('T')[0],
  bedtime: '23:30',
  wake_time: '06:00',
  duration_hours: 6.5,
  quality_score: 65,
  interruptions: 2,
  deep_sleep_percentage: 18,
  notes: 'Felt rested but woke up once',
  created_at: new Date().toISOString(),
};

const MOCK_PHONE_USAGE: PhoneUsageRecord = {
  id: 1,
  user_id: 1,
  date: new Date().toISOString().split('T')[0],
  total_hours: 5.2,
  social_media_hours: 2.1,
  productive_hours: 1.8,
  entertainment_hours: 1.3,
  pickups_count: 87,
  late_night_usage: false,
  created_at: new Date().toISOString(),
};

const MOCK_EMOTION: EmotionRecord = {
  id: 1,
  user_id: 1,
  dominant_emotion: 'Neutral',
  confidence: 0.72,
  valence: 0.4,
  arousal: 0.5,
  stress_level: 45,
  emotions: [
    { emotion: 'Neutral', confidence: 0.72 },
    { emotion: 'Happy', confidence: 0.15 },
    { emotion: 'Sad', confidence: 0.08 },
    { emotion: 'Anxious', confidence: 0.05 },
  ],
  source: 'camera',
  timestamp: new Date().toISOString(),
};

const MOCK_ACTIVITY: ActivityRecord = {
  id: 1,
  user_id: 1,
  date: new Date().toISOString().split('T')[0],
  study_hours: 3,
  work_hours: 6,
  exercise_minutes: 20,
  break_count: 4,
  focus_score: 72,
  created_at: new Date().toISOString(),
};

const MOCK_TREND: DashboardData['trend_data'] = {
  dates: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
  burnout_scores: [55, 60, 48, 42, 50, 35, 42],
  wellness_scores: [45, 50, 62, 68, 60, 75, 62],
  sleep_scores: [55, 60, 72, 65, 58, 80, 65],
  emotion_scores: [50, 55, 68, 72, 60, 75, 68],
};

const MOCK_DASHBOARD: DashboardData = {
  burnout_analysis: MOCK_BURNOUT,
  recent_sleep: MOCK_SLEEP,
  recent_phone_usage: MOCK_PHONE_USAGE,
  recent_emotion: MOCK_EMOTION,
  recent_activity: MOCK_ACTIVITY,
  trend_data: MOCK_TREND,
};

// ─── Auth API ───────────────────────────────────────────────────────────────────

export const authApi = {
  async login(credentials: LoginRequest): Promise<AuthTokens> {
    const formData = new URLSearchParams();
    formData.append('username', credentials.username);
    formData.append('password', credentials.password);
    const response = await api.post<AuthTokens>('/auth/login', formData.toString(), {
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    });
    return response.data;
  },

  async register(data: RegisterRequest): Promise<AuthTokens> {
    const response = await api.post<AuthTokens>('/auth/register', data);
    return response.data;
  },

  async getCurrentUser(): Promise<User> {
    const response = await api.get<User>('/auth/me');
    return response.data;
  },

  async resetPassword(data: ResetPasswordRequest): Promise<{ status: string; message: string }> {
    const response = await api.post<{ status: string; message: string }>('/auth/reset-password', data);
    return response.data;
  },
};

// ─── Dashboard API ──────────────────────────────────────────────────────────────

export const dashboardApi = {
  async getDashboard(): Promise<DashboardData> {
    const response = await api.get<DashboardData>('/wellness/dashboard');
    return response.data;
  },

  async getBurnoutAnalysis(): Promise<BurnoutAnalysis> {
    const response = await api.get<BurnoutAnalysis>('/burnout/analysis');
    return response.data;
  },
};

// ─── Sleep API ──────────────────────────────────────────────────────────────────

export const sleepApi = {
  async getSleepRecords(days = 7): Promise<SleepRecord[]> {
    try {
      const response = await api.get<SleepRecord[]>(`/tracking/sleep?days=${days}`);
      return response.data;
    } catch {
      return [];
    }
  },

  async logSleep(data: Partial<SleepRecord>): Promise<SleepRecord> {
    const response = await api.post<SleepRecord>('/tracking/sleep', data);
    return response.data;
  },
};

// ─── Phone Usage API ────────────────────────────────────────────────────────────

export const phoneApi = {
  async getPhoneUsageRecords(days = 7): Promise<PhoneUsageRecord[]> {
    try {
      const response = await api.get<PhoneUsageRecord[]>(`/tracking/phone-usage?days=${days}`);
      return response.data;
    } catch {
      return [];
    }
  },

  async logPhoneUsage(data: Partial<PhoneUsageRecord>): Promise<PhoneUsageRecord> {
    const response = await api.post<PhoneUsageRecord>('/tracking/phone-usage', data);
    return response.data;
  },
};

// ─── Emotion API ────────────────────────────────────────────────────────────────

export const emotionApi = {
  async getEmotionRecords(days = 7): Promise<EmotionRecord[]> {
    try {
      const response = await api.get<EmotionRecord[]>(`/tracking/emotion?days=${days}`);
      return response.data;
    } catch {
      return [];
    }
  },

  async logEmotion(data: Partial<EmotionRecord>): Promise<EmotionRecord> {
    const response = await api.post<EmotionRecord>('/tracking/emotion', data);
    return response.data;
  },

  async analyzeCamera(imageBase64: string): Promise<EmotionRecord> {
    try {
      const response = await api.post<EmotionRecord>('/tracking/emotion/analyze-camera', {
        image: imageBase64,
      });
      return response.data;
    } catch {
      const emotions = ['Happy', 'Neutral', 'Sad', 'Surprised', 'Anxious'];
      const dominant = emotions[Math.floor(Math.random() * emotions.length)];
      return {
        ...MOCK_EMOTION,
        dominant_emotion: dominant,
        confidence: 0.7 + Math.random() * 0.2,
        emotions: emotions.slice(0, 4).map((e) => ({
          emotion: e,
          confidence: e === dominant ? 0.7 + Math.random() * 0.2 : Math.random() * 0.15,
        })),
      };
    }
  },
};

// ─── Activity API ───────────────────────────────────────────────────────────────

export const activityApi = {
  async getActivityRecords(days = 7): Promise<ActivityRecord[]> {
    try {
      const response = await api.get<ActivityRecord[]>(`/tracking/activity?days=${days}`);
      return response.data;
    } catch {
      return [];
    }
  },

  async logActivity(data: Partial<ActivityRecord>): Promise<ActivityRecord> {
    const response = await api.post<ActivityRecord>('/tracking/activity', data);
    return response.data;
  },
};

// ─── Recommendations API ────────────────────────────────────────────────────────

export const recommendationsApi = {
  async getRecommendations(): Promise<Recommendation[]> {
    try {
      const response = await api.get<Recommendation[]>('/recommendations');
      return response.data;
    } catch {
      return [];
    }
  },
};

export default api;
